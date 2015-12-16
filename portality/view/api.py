'''
The oabutton API.
'''

from datetime import datetime, timedelta

import json, urllib2, uuid, requests

from flask import Blueprint, request, abort, make_response, redirect, current_app
from flask.ext.login import current_user

from portality.view.query import query as query
import portality.models as models
from portality.core import app
import portality.util as util

from functools import wraps, update_wrapper
from flask import g, request, redirect, url_for


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_anonymous():
            abort(401)
        return f(*args, **kwargs)
    return decorated_function


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator
    
    
blueprint = Blueprint('api', __name__)


# return the API endpoint
@blueprint.route('/', methods=['GET','POST'])
@util.jsonp
@crossdomain(origin='*')
def api():
    resp = make_response( json.dumps({
        "README": {
            "description": "Welcome to the openaccessbutton API.",
            "documentation": "https://openaccessbutton.org/docs",
            "version": "2.1"
        }
    }) )
    resp.mimetype = "application/json"
    return resp


@blueprint.route('/register', methods=['GET','POST'])
@util.jsonp
@crossdomain(origin='*')
def register():
    try:
        if request.json:
            vals = request.json
        else:
            vals = request.values
        # list the acceptable keys of a user object
        keys = ["username","name","email","profession","password"]
        # TODO: this should perhaps just call the account register functionality...
        # or account register should be dropped - have to check and see which is most suitable
        # check if account already exists and if so abort
        # TODO: this should explain why it is aborting
        exists = models.Account.pull(vals.get('email',''))
        if exists is not None:
            resp = make_response(json.dumps({'errors': ['username already exists']}))
            resp.mimetype = "application/json"
            return resp, 400
        user = models.Account()
        for k in vals.keys():
            # TODO: leaving this unchecked for now so we can test passing anything in
            #if k not in keys:
            #    abort(500)
            #else:
            user.data[k] = vals[k]
        if 'username' not in user.data:
            user.data['username'] = user.data['email']
        user.data['id'] = user.data['username']
        user.data['api_key'] = str(uuid.uuid4())
        # TODO: this should set a random 8 digit password string if one is not provided by the register API call
        user.set_password(vals.get('password',"password"))
        user.save()
        # TODO: trigger email account verification request
        resp = make_response(json.dumps({'api_key': user.data['api_key'], 'username': user.data['username']}))
        resp.mimetype = "application/json"
        return resp
    except Exception, e:
        resp = make_response(json.dumps({'errors': [str(e)]}))
        resp.mimetype = "application/json"
        return resp, 400


@blueprint.route('/retrieve', methods=['GET','POST'])
@util.jsonp
@crossdomain(origin='*')
def retrieve():
    try:
        if request.json:
            vals = request.json
        else:
            vals = request.values
        if 'email' in vals:
            exists = models.Account.pull_by_email(vals['email'])
        elif 'username' in vals:
            exists = models.Account.pull(vals['username'])
            if exists is None:
                exists = models.Account.pull_by_email(vals['username'])
        else:
            abort(404)
        if exists is not None:
            if exists.check_password(vals.get('password','')):
                # temporary method for recording that a trust OA user was logged in this way
                try:
                    if 'trust' in request.values:
                        if 'trust_login_date' not in exists.data: exists.data['trust_login_date'] = []
                        exists.data['trust_login_date'].append( datetime.now().strftime("%Y-%m-%d %H%M") )
                        exists.save()
                except:
                    pass
                resp = make_response(json.dumps({'api_key': exists.data.get('api_key','NONE'), 'username': exists.id}))
                return resp
            else:
                abort(401)
        else:
            abort(404)
    except Exception, e:
        resp = make_response(json.dumps({'errors': [str(e)]}))
        resp.mimetype = "application/json"
        return resp, 400


@blueprint.route('/blocked', methods=['GET','POST'])
@blueprint.route('/blocked/<bid>', methods=['GET','PUT','POST','DELETE'])
@util.jsonp
@login_required
@crossdomain(origin='*')
def blocked(bid=None):
    if bid is not None:
        e = models.Blocked.pull(bid)
        if request.method in ['PUT','POST','DELETE'] and current_user.id != e.data['author']:
            abort(401)
        if request.method in ['PUT','POST']:
            if request.json:
                vals = request.json
            else:
                vals = request.values
            if request.method == 'POST':
                for k, v in vals.items():
                    if k not in ['submit']:
                        e.data[k] = v
            elif request.method == 'PUT':
                # TODO: there may be things that should not be allowed to be overwritten here
                e.data = vals
            e.save()
        elif request.method == 'DELETE':
            e.delete()
        resp = make_response( json.dumps( "" if request.method == 'DELETE' else e.data ) )
        resp.mimetype = "application/json"
        return resp
    else:
        try:
            if request.json:
                vals = request.json
            else:
                vals = request.values
            event = models.Blocked()
            for k, v in vals.items():
                if k not in ['submit']:
                    event.data[k] = v
            '''event.data['coords_lat'] = vals.get('coords_lat','')
            event.data['coords_lng'] = vals.get('coords_lng','')
            event.data['doi'] = vals.get('doi','')
            event.data['url'] = vals.get('url','')
            event.data['user_id'] = current_user.id
            event.data['user_name'] = current_user.data.get('username','')
            event.data['user_profession'] = current_user.data.get('profession','')'''
            event.save()
            # call the status api and save the output for this URL
            _status(vals['url'], vals=vals)
            
            resp = make_response( json.dumps( {'url':vals.get('url',''), 'id':event.id } ) )
            resp.mimetype = "application/json"
            return resp
        except Exception, e:
            resp = make_response(json.dumps({'errors': [str(e)]}))
            resp.mimetype = "application/json"
            return resp, 400

        
@blueprint.route('/wishlist', methods=['GET','POST'])
@util.jsonp
@login_required
@crossdomain(origin='*')
def wishlist():
    try:
        if request.json:
            vals = request.json
        else:
            vals = request.values
        wish = models.Wishlist()
        wish.data['url'] = vals.get('url','')
        wish.data['user_id'] = current_user.id
        wish.save()
        resp = make_response( json.dumps( {'url':vals.get('url',''), 'id':wish.id } ) )
        resp.mimetype = "application/json"
        return resp
    except Exception, e:
        resp = make_response(json.dumps({'errors': [str(e)]}))
        resp.mimetype = "application/json"
        return resp, 400


@blueprint.route('/request', methods=['POST'])
@blueprint.route('/request/<rid>', methods=['POST'])
@util.jsonp
@login_required
@crossdomain(origin='*')
def req(rid=None):
    try:
        if request.json:
            vals = request.json
        else:
            vals = request.values
        if rid:
            rq = models.Request.pull(rid)
            if rq is None: abort(404)
            # TODO this should be a receipt of the article we want, either a file or a link to it
            # or an explanation as to why it is not being provided - update the request with the information
            # look for the url in our catalogue, find metadata about it, and record somewhere that we now have a stored copy of it
            # also should users who have this url on their requests or wishlist receive an email saying it is in?
        else:
            # TODO check how many requests this user has made in the last X
            # disallow if above rate limit X
            if False:
                resp = make_response( json.dumps( {'refused': 'user has reached request limit' } ) )
                resp.mimetype = "application/json"
                return resp, 403
                
            rq = models.Request()
            rq.data['url'] = vals.get('url','')
            rq.data['author'] = vals.get('author',[])
            if not isinstance(rq.data['author'],list) and ',' in rq.data['author']: rq.data['author'] = rq.data['author'].split(',')
            rq.data['email'] = vals.get('email','')
            if not isinstance(rq.data['email'],list) and  ',' in rq.data['email']: rq.data['email'] = rq.data['email'].split(',')
            rq.data['user_id'] = current_user.id

            # check if we have already emailed one of these authors about this url
            found = False
            for e in rq.data['email']:
                check = models.Request.check(e, rq.data['url'])
                if check.hits.total != 0 and not found:
                    resp = make_response( json.dumps( {'info':'already exists, added to user wishlist', 'url':vals.get('url',''), 'id':check['hits']['hits'][0]['_source']['id'] } ) )
                    # TODO add this url to this user wishlist (and update wishlist display to track requests sent)
                    found = True
            if not found:
                rq.save()
                # send an email to the author!
                resp = make_response( json.dumps( {'url':vals.get('url',''), 'id':rq.id } ) )
            resp.mimetype = "application/json"
            return resp
    except Exception, e:
        resp = make_response(json.dumps({'errors': [str(e)]}))
        resp.mimetype = "application/json"
        return resp, 400


@blueprint.route('/status', methods=['GET','POST'])
@util.jsonp
@login_required
@crossdomain(origin='*')
def status():
    try:
        if request.json:
            vals = request.json
        else:
            vals = request.values
            
        url = vals.get('url',False)
        if not url: abort(404)

        res = _status(url, vals=vals)
        
        resp = make_response(json.dumps(res))
        resp.mimetype = "application/json"
        return resp

    except Exception, e:
        resp = make_response(json.dumps({'errors': [str(e)]}))
        resp.mimetype = "application/json"
        return resp, 400


# TODO: can expose specific status functions with their own route
@blueprint.route('/processor/core/<value>', methods=['GET','POST'])
@util.jsonp
@login_required
@crossdomain(origin='*')
def core(value):
    try:
        resp = make_response(json.dumps( _core(value) ))
        resp.mimetype = "application/json"
        return resp
    except Exception, e:
        resp = make_response(json.dumps({'errors': [str(e)]}))
        resp.mimetype = "application/json"
        return resp, 400


@blueprint.route('/test/cleanup', methods=['GET','POST'])
@util.jsonp
@crossdomain(origin='*')
def testcleanup():
    try:
        # get all accounts starting with test_ and delete them (which removes their blocks and wishlists too)
        r = models.Account.query(q='id:test_*', size=1000000)
        rs = []
        for u in r['hits']['hits']:
            rs.append(u['_source']['id'])
            a = models.Account.pull(u['_source']['id'])
            a.delete()
        resp = make_response(json.dumps( rs ))
        resp.mimetype = "application/json"
        return resp
    except Exception, e:
        resp = make_response(json.dumps({'errors': [str(e)]}))
        resp.mimetype = "application/json"
        return resp, 400


def _status(url, vals={}, rerun=False):
    # find out the block count for this url and anything else we already know about it
    b = models.Blocked.count(url)
    w = models.Wishlist.count(url)
    # look for a save of this record
    found = models.Catalogue.pull_by_url(url)
    if found is not None and not rerun:
        result = found.data
        result['blocked'] = b
        result['wishlist'] = w
        return result
    else:
        result = {
            'url': url,
            'blocked': b,
            'wishlist': w
        }
        
        # quickscrape the url via contentmine, unless it is already in contentmine
        cm = _contentmine(url)
        result['contentmine'] = cm
                
        # look for further information if not already known, by calling the core processor
        if 'title' in cm.get('metadata',{}):
            t = cm['metadata']['title']
        elif 'title' in vals:
            t = vals['title']
        else:
            t = False
        if t:
            #TODO: make a proper ignore list and strip any non-az09 characters
            qv = " AND ".join([ i for i in cm['metadata']['title'].replace(',','').split(' ') if i not in ['and','or','in','of','the','for']][0:3])
            result['core'] = _core(qv)
        
        if 'doi' in vals:
            result['crossref'] = _crossref(vals['doi'])
        elif 'doi' in cm.get('metadata',{}):
            result['crossref'] = _crossref(cm['metadata']['doi'])
        
        if found is None:
            found = models.Catalogue()
        else:
            result.data['id'] = found.id
            result.data['created_date'] = found.data['created_date']
        found.data = result
        found.save()
        return result
        # academia.edu, researchgate, mendeley?
        # look via other processors if available, and if further info may still be useful
        # contentmine - put in the text miners I wrote to contentmine API, and can submit any articles for processing if not done already
        # oag - look for the article licensing criteria
        # oarr - find relevant repositories?
        # doaj - can query for journal article by doi or url and get back the article metadata including fulltext link
        # crossref - get some metadata?


def _core(value):
    url = app.config['PROCESSORS']['core']['url'].rstrip('/') + '/'
    api_key = app.config['PROCESSORS']['core']['api_key']
    addr = url + value
    addr += "?format=json&api_key=" + api_key
    response = requests.get(addr)
    try:
        data = response.json()
        result = {}
        if 'ListRecords' in data and len(data['ListRecords']) != 0:
            record = data['ListRecords'][1]['record']['metadata']['oai_dc:dc']
            result['author'] = record["dc:creator"].replace(' and ',', ').split(', ')
            result['url'] = 'http://core.kmi.open.ac.uk/download/pdf/' + data['ListRecords'][1]['record']['header']['header:content']['identifier'] + '.pdf'
            result['title'] = record["dc:title"]
        return result
    except:
        return {}


def _contentmine(value):
    # check to see if it is in contentmine
    url = app.config['PROCESSORS']['contentmine']['url'].rstrip('/') + '/'
    api_key = app.config['PROCESSORS']['contentmine'].get('api_key','')
    addr = url + 'processor/quickscrape?'
    addr += 'url=' + value + '&'
    addr += 'scraper=generic_open&'
    if api_key: addr += "api_key=" + api_key + '&'
    response = requests.get(addr)
    # if not get contentmine to quickscrape it
    # then return the metadata about it
    try:
        rs = response.json()
        if isinstance(rs,list):
            return rs[0]
        else:
            return rs
    except Exception, e:
        return {"errors": [str(e)]}


def _crossref(value):
    # check to see if it is in contentmine
    url = 'http://data.crossref.org/' + value
    response = requests.get(url, headers={'accept':'application/json'})
    # if not get contentmine to quickscrape it
    # then return the metadata about it
    try:
        return response.json()
    except Exception, e:
        return {"errors": [str(e)]}

