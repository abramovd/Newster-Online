from app import app
from flask import render_template, g, redirect, url_for, request
from forms import SearchForm

@app.route('/')
@app.route('/index')
def index():
    if g.search_form.validate_on_submit():
        redirect(url_for('search'))
    return render_template("index.html",
                           title= 'Home')
                           
@app.before_request
def before_request():
    g.search_form = SearchForm()
    
@app.route('/search', methods=['POST'])
def search():
    if not g.search_form.validate_on_submit():
        return redirect(url_for('index'))
    try: 
        method = request.form['algorithm']
        n_clusters = request.form['clusters']
    except:
        return redirect(url_for('index'))
    return redirect(url_for('search_results', method = method, n_clusters = n_clusters, query=g.search_form.search.data))

@app.route('/search_results/<query>?=<method>?=<n_clusters>')          
def search_results(method, n_clusters, query):
    from tools.newster.base import Newster
    from tools.newster.config import api_urls, api_keys
    try:
        newster = Newster(api_urls, api_keys, query)
        snippets = newster.get_snippets()
        titles = newster.get_titles()
        links = newster.get_links()
        sources = newster.get_sources()
        tags = []
        good_clusters = 0
        err = 'ok'
        try:
            clusters = newster.find_clusters(method = method, n_clusters = int(n_clusters))
            if method == 'stc':
                good_clusters = newster.get_number_of_good_clusters()
            if method != 'ward':
                tags = newster.get_common_tags(2)
        except Exception, e:
            clusters = {}
            err = str(e)
    except Exception, e:
        titles = []
        links = []
        snippets = []
        titles = []
        sources = []
        tags = []
        good_clusters = 0
        clusters = {}
        err = str(e)
    return render_template("search_results.html",
                           title='Search Results',
                           query = query,
                           snippets = snippets,
                           titles = titles,
                           clusters = clusters,
                           links = links,
                           sources = sources,
                           n_clusters = int(n_clusters),
                           method = method, tags = tags,
                           good_clusters = good_clusters,
                           err = err)