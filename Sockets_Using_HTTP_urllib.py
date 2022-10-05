# Pyhon produced urllib to make Socket and HTTP communications alot better.
# 3 lines code to retrive web data and use it as a (by using HTTP urllib as a socket).

import urllib.request
request_url = urllib.request.urlopen('https://www.geeksforgeeks.org/')
print(request_url.read())

# instead of open() we use openurl() as if its not a webpage but a file, and we treat it as a file.
# it can be a html file or a text file, etc
