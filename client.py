# USE THIS IN NODEMCU --------------------------------------------------------------------

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.21.73",5000))

myId = "633ea81e036440ee00ede2a2"
while True:
    message = myId.encode('utf-8')
    client.send(message)
    msg = client.recv(1024).decode('utf-8')
    print(msg[14:15])
    print(msg[len(msg)-2:len(msg)-1])