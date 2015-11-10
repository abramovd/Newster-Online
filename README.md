# Newster Online
**Newster Online** is a Flask application based on [Newster](https://github.com/abramovd/Newster) package which is used for searching news on such websites as The Guardian and The New York Times. It returns the search results not in a common listed form (e.g. Google Search), but it uses some clustering techinuques to automaically divide results into groups based on news snippets.


### Supported Algorithms

Now newster supports next clustering algorithms:

* K-Means Clustering
* Ward's Hierarchical Clustering Method
* Suffix Tree Clustering
* Formal Concept Analysis Algorithm Based on Probability Index

Besides, there is a standard listed representation of search results.

### Installation

In order to install Newster Online on your local machine you need to complete the following steps in your terminal.

#### _Step 1_

Clone this git repo there:

```sh
$ git clone https://github.com/abramovd/Newster-Online.git
```
Now you have ```Newster-Online``` folder in your current directory, move there:
```sh
$ cd Newster-Online
```

#### _Step 2_

Newster Online based on Newster package, so now you need to install this submodule with git:
```sh
$ git submodule init
$ git submodule update
```
Afrter this you will have Newster submodule installed in ```app/tools``` folder.

#### _Step 3_

Now you need to install all the dependencies listed in ```requirements.txt``` and ```conda-requirements.txt``` with Pip:

```sh
$ pip install -r requirements.txt
$ pip install -r conda-requirements.txt
```

This may require admin permissions on your machine (and should then be run with sudo).

Now you can run the server from the root directory with **python**:

```sh
$ python run.py
```

or with **gunicorn**:
```sh
$ gunicorn app:app
```

If you run with gunicorn and have ```ERROR: Connection in use```. You need to kill all previuos gunicorn processes. Too see all the runnung processes run ```ps ``` command in terminal and after that ```kill``` all the gunicron processes (maybe you will need ```-9``` flag).

OK. After you open ```127.0.0.1:5000``` or ```127.0.0.1:8000``` on you web browser you can see the main page of Newster Online. However, when you try to query news you will get nothing back. This is because you need to specify your own API keys for news sources.

You need to get your own API keys on [the Guardian](http://open-platform.theguardian.com/access/) or/and [the New York Times](http://developer.nytimes.com/docs/reference/keys) websites. For NYT you need to register for Search Articles API.

After that you need to insert your API key(s) in the ```config.py``` file in the ```tools``` folder with Newster package. That's how this file looks like:

```python
guardURL = 'http://content.guardianapis.com/search?'
nytURL = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?'
key_g = '' # #insert your The Guardian api-key
key_nyt = '' # #insert your NYT api-key

api_urls = [guardURL, nytURL]
api_keys = [key_g, key_nyt] 
```

If you want to use only one of the API's then you should edit ```api_urls``` and ```api_keys``` lists or change it from list to variable. For example, if you want to use only NYT API: ```api_urls = [nytURL]``` and ```api_keys = [key_nyt]``` or ```api_urls = nytURL``` and ```api_keys = key_nyt```.

OK. Now Newster Online should work just fine.

### Usage

Newster Online interface gives you an opportunity too choose what algorithms to run and specify the desired number of clusters. After you write your query in a text field and click "Search" you will see all the results. For every cluster Newster Online provides tags to describe grouped articles and explain its decision.

## Online Implementation
Newster Online is implemented on Heroku Server: newster2.herokuapp.com. If you see the message "Application Offline for Maintenance" you should get in touch with me: diabramo@ya.ru.

## Author
Dmitry Abramov &copy;