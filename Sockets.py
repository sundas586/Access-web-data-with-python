# To open a socket and retrieve the data. 

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() 

mysock.send(cmd)
while True:
    data = mysock.recv(512) # starts to read data we got
    if len(data) < 1:  # if the file ends, the length becomes < 1 
        break
    print(data.decode(),end='') # converting to uni-code

mysock.close()

'''GET http://data.pr4e.org/romeo.txt HTTP/1.0 -- (HTTP RULES)
\n -- (Followed by endline)
\n -- (Followed by empty line)
.encode() -- utf8 encoding''''
