from flask import render_template
from . import main 
from ..requests import get_news,get_headlines
from ..models import Newsource,Headlines

#Views 
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its date 
    '''
      # Getting news news 
    sources = get_news() 
  
    print(sources)
    title = 'Home - Welcome to News Highlight'
    return render_template('index.html',title = title , sources = sources)

@main.route('/news/<sources>')
def news(sources):

  '''
  View news page function that returns the news details page and its data
  '''

  news = get_headlines(sources)
  print(news)
  
  
  return render_template('news.html',news = news)
