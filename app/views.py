from app import app
from flask import render_template, g, redirect, url_for
from forms import SearchForm

@app.route('/')
@app.route('/index')
def index():
    form = SearchForm()
    if form.validate_on_submit():
        redirect(url_for('search_results'), form = form)
    return render_template("index.html",
                           title= 'Home', form = form)
                           
                           
                           
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
    from newster.base import Newster
    from newster.config import api_urls, api_keys
    try:
        newster = Newster(api_urls, api_keys, query)
        snippets = newster.get_snippets()
        titles = newster.get_titles()
        links = newster.get_links()
        sources = newster.get_sources()
        clusters = newster.find_clusters(method = 'kmeans', n_clusters = 10)
    except:
        titles = []
        snippets = []
    return render_template("search_results.html",
                           title='Search Results',
                           query = query,
                           snippets = snippets,
                           titles = titles,
                           clusters = clusters,
                           links = links,
                           sources = sources)  