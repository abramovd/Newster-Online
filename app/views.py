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
        newster = None
        newster = Newster(api_urls, api_keys, query)
        snippets = newster.get_snippets()
        titles = newster.get_titles()
        links = newster.get_links()
        sources = newster.get_sources()
        m = 'ok'
        try:
            newster = None
            newster = Newster(api_urls, api_keys, query)
            clusters = newster.find_clusters(method = method, n_clusters = int(n_clusters))
        except Exception, e:
            clusters = {}
            m = str(e)
    except:
        titles = []
        links = []
        snippets = []
        titles = []
        sources = []
        clusters = {}
    return render_template("search_results.html",
                           title='Search Results',
                           query = query,
                           snippets = snippets,
                           titles = titles,
                           clusters = clusters,
                           links = links,
                           sources = sources,
                           n_clusters = int(n_clusters),
                           method = method, m = m)  