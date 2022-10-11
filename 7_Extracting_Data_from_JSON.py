#  read the JSON data from a URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file.
import urllib.request
import json
import ssl

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("URL please : ")
request_url = urllib.request.urlopen(url) # create a handle/ socket to send GET request
jsonData = request_url.read().decode()    # read and decode the obtained responce data
a = 0
pythonData = json.loads(jsonData)         # converts json to python dictionary
for items in pythonData["comments"] :
    a = a + items["count"]
print(a)



