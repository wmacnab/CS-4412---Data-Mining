# the script selects all tags on the front page that have the src attribute, and then cleans and normalizes the URLs to get an absolute path for each download ...
# ... making sure to discard external links. Then, each file is downloaded to its own path in the local folder downloaded on your own machine

# notice Python's os module is used briefly to retrieve the target directory for each download and create missing directories along the path if needed.
# the os module acts as an interface between Python and the operating system, allowing it to manipulate file paths, create directories, get information ...
# ... about running processes and environment variables, and many other useful things

import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = 'downloaded'
baseUrl = 'http://pythonscraping.com'

def getAbsoluteURL(baseUrl, source):
    if source.startswith('http://www.'):
        url = 'http://{}'.format(source[11:])
    elif source.startswith('http://'):
        url = source
    elif source.startswith('www.'):
        url = source[4:]
        url = 'http://{}'.format(source)
    else:
        url = '{}/{}'.format(baseUrl, source)
    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace('www.', '')
    path = path.replace(baseUrl, '')
    path = downloadDirectory+path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)
    
    return path

html = urlopen('http://www.pythonscraping.com')
bs = BeautifulSoup(html, 'html.parser')
downloadList = bs.findAll(src=True)

for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download['src'])
    if fileUrl is not None:
        print(fileUrl)

# lambda function to select all tags on the front page that have the src attribute
urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))
