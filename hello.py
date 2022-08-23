#from turtle import ht
"""
import imp
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
    html = urlopen('http://pythonscraping.com/pages/page1.html') # returns file object
except HTTPError as e:
    print(e)
    # return null, break, or do some other "Plan B"
except URLError as e:
    print('The server could not be found!')
else:
    print('It Worked!')
    # program continues. Note: If you return or break in the exception catch, you do not need to use the "else" statement

# a BeautifulSoup object with parameters HTML text object, and the second is the parser bs will use
#bs = BeautifulSoup(html.read(), 'html.parser')
bs = BeautifulSoup(html, 'html.parser')
print(bs)
"""