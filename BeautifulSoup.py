# Using BeautifulSoup library, to retrieve and parse HTML and pull out anchor tags.

import urllib.request, urllib.parse, urllib.error   # HTML library
from bs4 import BeautifulSoup                       # library to parse HTML
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')                             # Asking for desired URLR
html = urllib.request.urlopen(url, context=ctx).read()  # creating Handle to pass the URL # socket
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))                    # retrieve a anchor tag or retrieve None
   
    # hence beautiful soap is making it easy for us to parse through HTML syntax, with out using regular expression
