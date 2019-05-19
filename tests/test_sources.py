import unittest 
from app.models import newsource
Newsource = newsource.Newsource

class NewsourceTest(unittest.TestCase):
  '''
  Test class to test the behaviour of the Newsource class
  '''

  def setUp(self):
    '''
    Set up method that will run before every Test 
    '''
    self.new_News = Newsource('abc-news','ABC News','Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.','https://abcnews.go.com')

  def test_instance(self):
      self.assertTrue(isinstance(self.new_News,Newsource))


if __name__ == ' __main__':
    
