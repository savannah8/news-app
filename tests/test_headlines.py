import unittest 
from app.models import Headlines
Headlines = headlines.Headlines

class HeadlinesTest(unittest.TestCase):
  '''
  Test class to test the behaviour of the headlines class
  '''

  def setUp(self):
    '''
    Set up method that will run before every Test 
    '''
    self.new_News = Headlines('bbc-news','BBC News', 'your trusted source for breaking news','a rasher of bacon ups cancer risk','Image','https://www.bbc.com/news/health-47947965')

  def test_instance(self):
      self.assertTrue(isinstance(self.new_Headlines,Headlines))


if __name__ == ' __main__':