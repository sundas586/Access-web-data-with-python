''''The program will use urllib to read the HTML from the data files below, extract the href= values from the anchor tags,
scan for a tag that is in a particular position from the top and follow that link, 
repeat the process a number of times, and report the last name you find.''''

import urllib.request
from bs4 import BeautifulSoup

url = input("Enter url-")
rep = int(input("Enter repeat count:"))
pos = int(input('Enter position'))

while rep > 0:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    print("Retrieving:", tags[pos-1].get("href", None))
    url = tags[pos-1].get("href", None)
    rep = rep - 1
    
    #HTTP LINK = http://py4e-data.dr-chuck.net/known_by_Alyia.html
