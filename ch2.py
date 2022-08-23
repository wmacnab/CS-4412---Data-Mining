from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup

try:
    html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
except HTTPError as e:
    print(e)
try:
    bs = BeautifulSoup(html.read(), 'html.parser') #grabs entire page and creates a BeautifulSoup object
except AttributeError as e:
    print(e)

nameList = bs.findAll('span', {'class':'green'}) # BeautifulSoup's find() and find_all() are two functions likely to be used a lot
for name in nameList:
    print(name.get_text()) #get_text() strips all tags and returns a Unicode string containing the text only. bs object is more powerful, this should be done last

#find_all(tag, attributes, recursive, text, limit, keywords)
#find(tag, attributes, recursive, text, keywords)
# tag can take a Python list
# attributes can take a Python dictionary

nameList = bs.find_all(text='the prince')
print(len(nameList))
