
from flask import Flask, request, abort, render_template, make_response, redirect, flash
from flask.views import View
from flask.ext.login import login_user, current_user

import json

import portality.models as models
import portality.util as util
from portality.core import app, login_manager

from portality.view.query import blueprint as query
from portality.view.stream import blueprint as stream
from portality.view.account import blueprint as account
from portality.view.api import blueprint as api
from portality.view.media import blueprint as media
from portality.view.pagemanager import blueprint as pagemanager
from portality.view.feed import blueprint as feed


app.register_blueprint(query, url_prefix='/query')
app.register_blueprint(stream, url_prefix='/stream')
app.register_blueprint(account, url_prefix='/account')
app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(media, url_prefix='/media')
app.register_blueprint(feed)
app.register_blueprint(pagemanager)


@login_manager.user_loader
def load_account_for_login_manager(userid):
    out = models.Account.pull(userid)
    return out

@app.context_processor
def set_current_context():
    """ Set some template context globals. """
    return dict(current_user=current_user, app=app)

@app.before_request
def standard_authentication():
    """Check remote_user on a per-request basis."""
    remote_user = request.headers.get('REMOTE_USER', '')
    if request.json:
        vals = request.json
    else:
        vals = request.values
    if remote_user:
        user = models.Account.pull(remote_user)
        if user is not None:
            login_user(user, remember=False)
    # add a check for provision of api key
    elif 'api_key' in vals:
        res = models.Account.query(q='api_key:"' + vals['api_key'] + '"')['hits']['hits']
        if len(res) == 1:
            user = models.Account.pull(res[0]['_source']['id'])
            if user is not None:
                login_user(user, remember=False)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(401)
def unauthorised(e):
    return render_template('401.html'), 401
        

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/download")
def dlredir():
    return redirect('/#download')


@app.route("/docs")
def docs():
    return render_template("docs.html")


@app.route("/bookmarklet")
def bookmarklet():
    return render_template("bookmarklet.html")


@app.route("/wishlist")
def wishlist():
    try:
        if request.json:
            vals = request.json
        else:
            vals = request.values
        resp = make_response(json.dumps( current_user.wishlist(**vals) ))
        resp.mimetype = "application/json"
        return resp
    except:
        abort(404)

@app.route("/blocked")
def blocked():
    try:
        if request.json:
            vals = request.json
        else:
            vals = request.values
        resp = make_response(json.dumps( current_user.blocked(**vals) ))
        resp.mimetype = "application/json"
        return resp
    except:
        abort(404)


@app.route("/stories")
def map():
    return render_template("map.html")

@app.route("/story")
def searchstory():
    return render_template("searchstory.html")

@app.route("/story/<path:sid>")
def story(sid):
    story = models.Blocked.pull(sid.replace('.json',''))
    #story = models.Record.pull(sid.replace('.json',''))
    turl = None
    cat = None
    user = None
    if story is not None:
        about = story.about(sid.replace('.json',''), exclude=story.id)
        turl = story.data['url']
        user = models.Account.pull(story.data['author'])
    else:
        about = models.Record.about(sid.replace('.json',''))
        if about.get('hits',{}).get('total',0) == 0:
            flash('Sorry, there was no story found about ' + sid, 'warning')
            return redirect('/story')
        else:
            turl = about['hits']['hits'][0]['_source']['url']
    if turl is not None:
        c = models.Catalogue.pull_by_url(turl)
        if c is not None:
            cat = c.data
    if util.request_wants_json() or sid.endswith('.json'):
        resp = make_response( story.json )
        resp.mimetype = "application/json"
        return resp    
    else:
        # TODO this should not pass all user data, some of that should be stored with the story
        return render_template("story.html", story=story, about=about, catalogue=cat, user=user.data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=app.config['PORT'])

