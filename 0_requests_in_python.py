#The "requests" module is a third-party library used for making HTTP requests in Python.<br/>
#The module provides a simple way to make requests to URLs, and it handles many of the details of managing HTTP connections and sending HTTP requests and responses.<br/>

#Here is an example of how to use the requests module to send a GET request to a URL and print the response:<br/>

import requests

response = requests.get('https://www.example.com')
print(response.content)

#In this example, we first import the requests module, then we use the get() function to send a GET request to the URL "https://www.example.com".<br/>
#The get() function returns a Response object that contains the server's response to our request.<br/>
#We then print the content of the response using the content attribute of the Response object.<br/>

############# An API avaiable on internet to get the location of any city ############

import requests

city = input("Enter a city name: ")

# Make a request to OpenWeatherMap API to get the location data
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY")

# Check if the request was successful
if response.status_code == 200:
    # Get the JSON data from the response
    data = response.json()
    # Extract the latitude and longitude from the data
    lat = data['coord']['lat']
    lon = data['coord']['lon']
    # Print the location data
    print(f"The location of {city} is: ({lat}, {lon})")
else:
    print(f"Error: {response.status_code}")

