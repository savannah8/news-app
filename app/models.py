class Headlines:
  '''
  Headlines class to define Headline Objects 
  '''

  def __init__(self,id,author,title,description,urlToImage,url):

      self.id = id
      self.author = author 
      self.title = title 
      self.description = description 
      self.urlToImage = urlToImage
      self.url = url


class Newsource:
  '''
  Newsource class to define News Objects 
  '''

  def __init__(self,id,name,description,url,):
      self.id = id
      self.name = name 
      self.description = description 
      self.url = url
