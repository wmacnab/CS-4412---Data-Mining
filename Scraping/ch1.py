from tempfile import TemporaryFile
from urllib.request import urlopen
from urllib.error import HTTPError
from  bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title == None:
    print('Title could not be found')
else:
    print(title)

"""
When writing scrapers, it’s important to think about the overall pattern of your code
in order to handle exceptions and make it readable at the same time. You’ll also likely
want to heavily reuse code. Having generic functions such as getSiteHTML and
getTitle (complete with thorough exception handling) makes it easy to quickly—
and reliably—scrape the web.
"""
