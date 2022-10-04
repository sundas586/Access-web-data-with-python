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

In the following code of lines we do a HTTP request to server using python :
- Build a connection **(Socket/ TCP connection)**
- Ask the desired data through web browser **(GET REQUEST)**
- Recieve the desired data from server **(RESPONCE)**

![5](https://user-images.githubusercontent.com/33677647/193856682-5b556eda-5bae-406d-ac6b-0fafb91d2fab.PNG)

