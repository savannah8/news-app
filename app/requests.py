
import urllib.request,json
from .models import Newsource,Headlines

# Getting api key
api_key = None
# Getting the news base url
base_url = None
headlines_url = None

def configure_request(app):
    global api_key,base_url,headlines_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    headlines_url = app.config['HEADLINES_API_BASE_URL']

def get_news():
    '''
    Function that gets the json to our url request
    '''

    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None 

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results

def process_results(news_list):
    '''
    Function that processes the news result and transform them to a list 
    of objects
    Args:
        news_list: A list of dictionaries that contain news sources 
    Returns :
          news_results: A list of news objects 
    '''
    
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get ('description')
        url = news_item.get('url')

    
        news_object = Newsource(id,name,description,url)
        news_results.append(news_object)

    return news_results

def get_headlines(sources):
    '''
    Function that gets the json to our url request
    '''
    get_headlines_url = headlines_url.format(sources,api_key)

    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        headlines_results = None 

        if get_headlines_response['articles']:
            headlines_results_list = get_headlines_response['articles']
            headlines_results = process_headlines(headlines_results_list)
 
    return headlines_results

def process_headlines(headlines_list):
    '''
    Function that processes the news result and transform them to a list 
    of objects
    Args:
        news_list: A list of dictionaries that contain news sources 
    Returns :
          news_results: A list of news objects 
    '''
    
    headlines_results = []
    for headlines_item in headlines_list:
        id = headlines_item.get('id')
        author = headlines_item.get('author')
        title = headlines_item.get ('title')
        description = headlines_item.get('description')
        urlToImage = headlines_item.get ('urlToImage')
        url = headlines_item.get ('url')

        if urlToImage:

            headlines_object = Headlines(id,author,title,description,urlToImage,url)
            headlines_results.append(headlines_object)

    return headlines_results
