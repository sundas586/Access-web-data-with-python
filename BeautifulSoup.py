# Using BeautifulSoup library, to retrieve and parse HTML and pull out anchor tags.

import urllib.request, urllib.parse, urllib.error   # HTML library
from bs4 import BeautifulSoup                       # library to parse HTML 

url = input('Enter - ')                             # Asking for desired URLR
html = urllib.request.urlopen(url, context=ctx).read()  # creating Handle to pass the URL # socket
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))                    # retrieve a anchor tag or retrieve None
