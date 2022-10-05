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
- 
![Untitled-1](https://user-images.githubusercontent.com/33677647/194102295-aa77848c-d59c-4588-aaa4-703330861fd2.jpg)







