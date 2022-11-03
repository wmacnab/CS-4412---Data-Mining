#from urllib.request import urlopen
import urllib
from urllib.request import Request
from urllib.error import HTTPError
from bs4 import BeautifulSoup

url1 = 'http://pathofexile.com'
url2 = 'http://accesslaundry.com'
url3 = 'http://twitter.com'
url4 = 'http://georgia.gov'


try:
    url = Request(url1, headers = {'User-Agent' : 'Magic Browser'})
    htmlContent = urllib.request.urlopen(url)
    print(type(htmlContent))
except HTTPError as e:
    print(e)


soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify())

idk = soup.find_all('h2')
print(type(idk))
for i in idk:
    print(i)
