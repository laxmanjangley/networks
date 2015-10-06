import socket
import sock

connection = sock.mysocket()
connection.connect("www.iitd.ac.in",80)
f=open("request",'r')

connection.mysend(f.read())
a= connection.myreceive()

connection.mysend(f.read())
b=connection.myreceive()
print len(a),len(b)
