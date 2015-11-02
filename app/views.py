from app import app
from flask import render_template, g, redirect, url_for
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
    return redirect(url_for('search_results', query=g.search_form.search.data))


@app.route('/search_results/<query>')          
def search_results(query):
    from tools.newster.base import Newster
    from tools.newster.config import api_urls, api_keys
    titles = []
    links = []
    snippets = []
    titles = []
    sources = []
    clusters = {}
    n_clusters = 7
    try:
        newster = Newster(api_urls, api_keys, query)
        snippets = newster.get_snippets()
        titles = newster.get_titles()
        links = newster.get_links()
        sources = newster.get_sources()
        clusters = newster.find_clusters(method = 'fca', n_clusters = n_clusters)
    except:
        pass
    return render_template("search_results.html",
                           title='Search Results',
                           query = query,
                           snippets = snippets,
                           titles = titles,
                           clusters = clusters,
                           links = links,
                           sources = sources,
                           n_clusters = n_clusters)  