import os

class Config:
  '''
  General configuration parent class 
  '''
  NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey=dc5d7f99fdd447759cb8618e8c5c17a9'
  HEADLINES_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=dc5d7f99fdd447759cb8618e8c5c17a9'

  NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
class ProdConfig(Config):
  '''
  Production configuration child class
  Args:
      Config: The parent configuration class with General configuration settings 
  '''
  pass

class DevConfig(Config):
  '''
  Development configuration child class 
  Args:
    Config: The parent configuration class with General configuration settings 
  '''

  DEBUG = True

config_options = {
  'development':DevConfig,
  'production':ProdConfig
}
