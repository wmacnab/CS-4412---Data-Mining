# images
#looking at the file path of images can be more reliable

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})
for image in images:
    print(image['src'])

# with tag objects, a Python list of attributes can be ...
# ... automatically accessed by calling this:
# myTag.attrs

# lambda expression: a function passed into another func as a var
# BeautifulSoup allows funct param passing into find_all()
# the func must take a Tag object as an argument and return bool
# for example, the following retrieves all tags with 2 attributes:
# bs.find_all(lambda tag: len(tag.attrs) == 2)