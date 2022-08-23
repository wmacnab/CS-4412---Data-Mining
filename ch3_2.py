# A single function, getLinks, that takes a Wikipedia article URL
# of the form /wiki/<Article_Name> and returns a list of all linked
# article URLs in the same form

# A main function that calls getLinks with a starting article,
# chooses a random article link from the returned list, and calls
# getLinks again, until you stop the program or until no article
# links are found on the new page

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)

