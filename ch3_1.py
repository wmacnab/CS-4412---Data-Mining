# Chapter 3 - Writing Web Crawlers

# A Python script that retrives an arbitrary Wikipedia page and ...
# ... produces a list of links on that page

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re # regex

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
#for link in bs.find_all('a'):
for link in bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])

# article pages on Wikipedia reside within the div with
# ... the id set to bodyContent. The URLs do not contain
# ... colons and they begin with /wiki/
