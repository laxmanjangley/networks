import socket
import sock
import sys

s = sock.mysocket()
s.sock.connect(('localhost',int(sys.argv[1])))
s.sock.send("yoyoy\n")
s.sock.shutdown(socket.SHUT_RDWR)
s.sock.connect(('localhost',int(sys.argv[1])))
s.sock.send("yoyoy010\n")
