# ========================
# MAIN SETTINGS

# make this something secret in your overriding app.cfg
SECRET_KEY = "default-key"

# contact info
ADMIN_NAME = "Cottage Labs"
ADMIN_EMAIL = "sysadmin@openaccessbutton.org"

# service info
SERVICE_NAME = "Open Access Button"
SERVICE_TAGLINE = ""
HOST = "0.0.0.0"
DEBUG = True
PORT = 5004

# elasticsearch settings
ELASTIC_SEARCH_HOST = "http://127.0.0.1:9200" # remember the http:// or https://
ELASTIC_SEARCH_DB = "oabutton"
INITIALISE_INDEX = True # whether or not to try creating the index and required index types on startup

# list of superuser account names
SUPER_USER = ["test"]

# Can people register publicly? If false, only the superuser can create new accounts
PUBLIC_REGISTER = True

# can anonymous users get raw JSON records via the query endpoint?
PUBLIC_ACCESSIBLE_JSON = True 


# ========================
# MAPPING SETTINGS

# a dict of the ES mappings. identify by name, and include name as first object name
# and identifier for how non-analyzed fields for faceting are differentiated in the mappings
FACET_FIELD = ".exact"
MAPPINGS = {
    "record" : {
        "record" : {
            "dynamic_templates" : [
                {
                    "default" : {
                        "match" : "*",
                        "match_mapping_type": "string",
                        "mapping" : {
                            "type" : "multi_field",
                            "fields" : {
                                "{name}" : {"type" : "{dynamic_type}", "index" : "analyzed", "store" : "no"},
                                "exact" : {"type" : "{dynamic_type}", "index" : "not_analyzed", "store" : "yes"}
                            }
                        }
                    }
                }
            ]
        }
    }
}
MAPPINGS['account'] = {'account':MAPPINGS['record']['record']}
MAPPINGS['blocked'] = {'blocked':MAPPINGS['record']['record']}
MAPPINGS['wishlist'] = {'wishlist':MAPPINGS['record']['record']}
MAPPINGS['pages'] = {'pages':MAPPINGS['record']['record']}
MAPPINGS['catalogue'] = {'catalogue':MAPPINGS['record']['record']}


# ========================
# QUERY SETTINGS

# list index types that should not be queryable via the query endpoint
NO_QUERY = ['account']

# list additional terms to impose on anonymous users of query endpoint
# for each index type that you wish to have some
# must be a list of objects that can be appended to an ES query.bool.must
# for example [{'term':{'visible':True}},{'term':{'accessible':True}}]
ANONYMOUS_SEARCH_TERMS = {
    "pages": [{'term':{'visible':True}},{'term':{'accessible':True}}]
}

# a default sort to apply to query endpoint searches
# for each index type that you wish to have one
# for example {'created_date' + FACET_FIELD : {"order":"desc"}}
DEFAULT_SORT = {
    "pages": {'created_date' + FACET_FIELD : {"order":"desc"}}
}


# ========================
# PROCESSOR SETTINGS
PROCESSORS = {
    "core": {
        "url": "http://core.kmi.open.ac.uk/api/search/",
        "api_key": ""
    },
    "contentmine": {
        "url": "http://contentmine.org/api/",
        "api_key": ""
    }
}


# ========================
# MEDIA SETTINGS

# location of media storage folder
MEDIA_FOLDER = "media"


# ========================
# PAGEMANAGER SETTINGS

# folder name for storing page content
# will be added under the templates/pagemanager route
CONTENT_FOLDER = "content"

# etherpad endpoint if available for collaborative editing
COLLABORATIVE = 'https://cottagelabs.com/sp'

# when a page is deleted from the index should it also be removed from 
# filesystem and etherpad (if they are available in the first place)
DELETE_REMOVES_FS = False # True / False
DELETE_REMOVES_EP = False # MUST BE THE ETHERPAD API-KEY OR DELETES WILL FAIL

# disqus account shortname if available for page comments
COMMENTS = ''


'''
    "searchables" : {
        "Google" : "http://www.google.com/search?q=",
        "Google scholar" : "http://scholar.google.com/scholar?q=",
        "Google video" : "http://www.google.com/search?tbm=vid&q=",
        "Google blogs" : "http://www.google.com/search?tbm=blg&q=",
        "Google books" : "http://www.google.com/search?tbm=bks&q=",
        "Google images" : "http://www.google.com/search?tbm=isch&q=",
        "Google search ResearcherID" : "http://www.google.com/search?q=XXXX+site%3Awww.researcherid.com",
        "Google search ACM Author Profiles" : "http://www.google.com/search?q=XXXX+ACM+author+profile+site%3Adl.acm.org",
        "Google search Mathemtatics Genealogy" : "http://www.google.com/search?q=XXXX+site%3Agenealogy.math.ndsu.nodak.edu",
        "Microsoft academic search" : "http://academic.research.microsoft.com/Search?query=",
        "Zentralblatt Math" : "http://www.zentralblatt-math.org/zmath/en/search/?q=",
        "Zentralblatt Math authors" : "http://www.zentralblatt-math.org/zmath/en/authors/?au=",
        "MathSciNet" : "http://www.ams.org/mathscinet-mref?ref=",
        "DOI resolver" : "http://dx.doi.org/",
        "PubMed" : "http://www.ncbi.nlm.nih.gov/pubmed?term=",
        "PubMed Central" : "http://www.ncbi.nlm.nih.gov/pmc/?term=",
        "BioMed Central" : "http://www.biomedcentral.com/search/results?terms="
    }

        var searcher = '<p style="text-align:right">search <select class="span2" id="extsrch_target">'
        searcher += '<option value="/search?q=">This site</option>'
        searcher += '<option value="/{{ objectrecord.owner }}/{{ objectrecord.collection }}?q=">The {{ objectrecord.collection }} collection</option>'
        var searchables = {{ searchables | safe }}
        for ( var item in searchables ) { searcher += '<option value="' + searchables[item] + '">' + item + '</option>'; }
        searcher += '</select><br />for <input class="span2" id="extsrch_value" />'
        jQuery('#searcher').append(searcher)
        var searchvals = {{ searchvals | safe }}
        jQuery('#extsrch_value').autocomplete({source:searchvals})

        var dosearch = function(event) {
            var target = jQuery('#extsrch_target').val()
            var value = jQuery('#extsrch_value').val()
            if ( target.match("XXXX") ) {
                var href = target.replace("XXXX",value)
            } else {
                var href = target + value
            }
            //window.open(href)
            window.location = href
        }
        var checkenter = function(event) {
            var keycode = (event.keyCode ? event.keyCode : event.which)
            if (keycode == '13') { dosearch(event) }
        }
'''