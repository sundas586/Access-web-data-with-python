# 3 lines code to retrive web data and use it as a (by using HTTP urllib as a socket).

import urllib.request
request_url = urllib.request.urlopen('https://www.geeksforgeeks.org/')
print(request_url.read())
