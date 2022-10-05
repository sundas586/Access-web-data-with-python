from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')

contents = []
summ = 0
for tag in tags:
    contents = int(tag.contents[0])
    summ += contents
print(summ)



# HTTP Link = http://py4e-data.dr-chuck.net/comments_42.html
