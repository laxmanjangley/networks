import socket
import sock
import sys

server = sock.mysocket()
server.sock.bind(("127.0.0.1",int(sys.argv[1])))
server.sock.listen(10)
conn,addr = server.sock.accept()
#print conn,addr
res = ""
while True:
    res+=conn.recv(1024)
    print res
