# Access-web-data-with-python

### Sockets / TCP Connections 

Sockets and the socket API are used to send messages across a network. They provide a form of inter-process communication (IPC).
A socket is one endpoint of a two-way communication link between two programs running on the network. 

![eee](https://user-images.githubusercontent.com/33677647/193822181-5e7a3291-06cc-4204-a5e0-511a9a3a3722.PNG)

A socket is bound to a port number so that the TCP layer can identify the application that data is destined to be sent to. An endpoint is a combination of an IP address and a port number.

Protocol = A ste of rules with which streams of data will be sent from one end to other.

IP Address = A unique IP address each time a connection is built between to ends, later it is removed.
<img width="1278" alt="python-socket-connection-diagram" src="https://user-images.githubusercontent.com/33677647/193822754-86792c12-0c7f-425f-a321-e33c48551243.png">
![1_oz_4rjYCgQzfz7sRncEUyQ](https://user-images.githubusercontent.com/33677647/193822835-251bcca1-2374-445a-91bf-44d8f79fc670.jpeg)
![udp-client-server-overview](https://user-images.githubusercontent.com/33677647/193822724-196a2705-6f14-43b5-9fea-ca001dc01bf0.png)
![common-ports-SocketProgramminginPython-Edureka](https://user-images.githubusercontent.com/33677647/193822811-ff5b8b27-0d1f-404a-822b-f91bd3388c1f.png)
![Uploading 1_oz_4rjYCgQzfz7sRncEUyQ.jpeg…]()
![udp-client-server-overview](https://user-images.githubusercontent.com/33677647/193823333-b12b27ca-2315-4502-8001-de679f610997.png)

## Hypertext Transfer Protocol

HTTP is a protocol for fetching resources such as HTML documents. It is the foundation of any data exchange on the Web and it is a client-server protocol, which means requests are initiated by the recipient, usually the Web browse

- In HTTP it is a rule that you have to request first, you can not get responce from server before

![diagram-of-http-communication-process](https://user-images.githubusercontent.com/33677647/193854230-5cdc0185-6b2f-4acd-978b-9134863923eb.png)
![1](https://user-images.githubusercontent.com/33677647/193856343-5f59c9bb-7949-470d-9493-576f46d82fe2.PNG)
![2](https://user-images.githubusercontent.com/33677647/193856381-b9057977-af40-4842-b42a-7f7920851f1b.PNG)
![3](https://user-images.githubusercontent.com/33677647/193856407-0c72de59-68cd-4355-bdf8-c00562686df6.PNG)
![4](https://user-images.githubusercontent.com/33677647/193856459-1e4bfa95-7dd7-463b-95ef-04ad62f5cd8d.PNG)
![request](https://user-images.githubusercontent.com/33677647/194102580-ac354826-1fc8-4f55-95a0-d18ff46feab3.png)


In the following code of lines we do a HTTP request to server using python :
- Build a connection **(Socket/ TCP connection)**
- Ask the desired data through web browser **(GET REQUEST)**
- Recieve the desired data from server **(RESPONCE)**

![5](https://user-images.githubusercontent.com/33677647/193856682-5b556eda-5bae-406d-ac6b-0fafb91d2fab.PNG)

## Unicode Characters and Strings

![a](https://user-images.githubusercontent.com/33677647/193957106-2176e8b7-9c71-43dd-9e36-b9672c17d8c3.PNG)

by default is .decode(utf-8) or .decode(ASCII) becaused utf-8 and ASCII both are compatible to each other.  
If its a old data, may be it is ASCII
If its new data, may be it is  UTF-8
As data is converted into bytes(by encoding) to travel over the internet

![a](https://user-images.githubusercontent.com/33677647/193957923-9b7a7db2-be0b-4f72-8ecd-dd4b32827634.PNG)

### ASCII AND UNICODE HISTORY

![1](https://user-images.githubusercontent.com/33677647/193958017-c409f064-9684-4660-a21d-3abebe816a9f.PNG)

Computers do not understand letters, they read numbers only, so we convert the letters into a ASCII code, for computer to read the letter,
the letter "p" has a ASCII code 112.
![2](https://user-images.githubusercontent.com/33677647/193958023-330abae6-5c3f-40fb-b03f-d4d28db49468.PNG)

But ASCII code is only for English letters, to let English and Chinese computer talk over the internet,
UNICODE was desigend, as unicode has lots and lots of characters.
utf-8 and ASCII are just same and compatible
![3](https://user-images.githubusercontent.com/33677647/193958026-3c52530d-9969-4238-908c-58feb8c11210.PNG)
![4](https://user-images.githubusercontent.com/33677647/193958036-b38992b8-7243-414b-b6d1-63cda658392d.PNG)

So, when you have a text like "Hi, this is a python3 statement \n Its october, 6:19 in the morning "
This text has only ABC, 123, \n, etc . So it is obviously ASCII code.
but when you encode it into bytes to send through internet,
and a Japanese computer recieves it,
they will use "UNICOde" to decode the English letters into there native letters.
as UNICODE has wide range of characters from several languages.

![a](https://user-images.githubusercontent.com/33677647/193960227-1a2d9052-0210-4e4d-88df-45409082eef1.PNG)

### import urllib.request

Pyhon produced urllib to make Socket and HTTP communications alot better.

### Data parsing

Data parsing is converting data from one format to another. Widely used for data structuring, it is generally done to make the existing, often unstructured, unreadable data more comprehensible. (import urllib.parser)

### Web Scraping

Web scraping is the process of collecting and parsing raw data from the Web.

- Find the URL that you want to scrape.
- Inspecting the Page.
- Find the data you want to extract.
- Write the code.
- Run the code and extract the data.
- Store the data in the required format


![Untitled-1](https://user-images.githubusercontent.com/33677647/194102295-aa77848c-d59c-4588-aaa4-703330861fd2.jpg)
![2](https://user-images.githubusercontent.com/33677647/194106402-72a58de3-05dc-43dc-8d41-da8233da3dde.PNG)
![5](https://user-images.githubusercontent.com/33677647/194106418-a9e02533-5d84-4095-aff3-c36324a893e6.PNG)
![6](https://user-images.githubusercontent.com/33677647/194106454-3013c02e-7db3-4c72-bf40-ee7a6b34f936.PNG)

### Web scraping vs Web crawling

![web-scraping-vs-web-crawling](https://user-images.githubusercontent.com/33677647/194105960-26d3be8b-3bb8-406b-a549-df7e81595a88.jpg)
<img width="1920" alt="4" src="https://user-images.githubusercontent.com/33677647/194105993-ac57c224-b37e-467f-95cd-e63eca45e440.png">
![3](https://user-images.githubusercontent.com/33677647/194106098-892225be-72cb-4539-a187-a2bf5312b7b8.PNG)

### Beautiful Soup

The biggest problem in sraping is the parsing of the HTML that comes back as responce.
And it turns out that when your browser retrieves HTML, it goes through a whole bunch of things that effectively forgives syntax errors in HTML. 
and then you fix that. And you realize after you try to fix this and you try to parse all the links that there is just so many variations and someone has already produced a solution. And it's a library called BeautifulSoup from a place called crummy.com

**Beautiful Soup is a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping.**
**Hence beautiful soap is making it easy for us to parse through HTML syntax, with out using regular expression**

# WIRE PROTOCOL

**The Wire Protocol is  how the data is put on the wire, or how the data leaves one system, transits a network, and then enters another system. And in that destination system**

The basic idea is that if we've got two programs, and they're going to communicate across the Internet. One is a Python program that's producing the data. Maybe it's reading a database, maybe it's reading a file. But inside it has a Python data structure, like a dictionary. And we want to send that across the network.the network is not Python. The network is not Java. The network is a data, And the other program is in Java, perhaps, our Python dictionary in other system needs to be a Java HashMap. 
We just have to send the data to the network on a specific **format** that we all agree on. **XML** , which is one of the **wire formats**.The data which is in a Python dictionary and we covert that data into to XML then send a person across the network,


