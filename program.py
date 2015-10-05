#!/usr/bin/python

#proxy pe nahi chalega.

from urlparse import urlparse
import socket               # Import socket module
import sys
import json
import os
import re
import sock


#os.environ['no_proxy']='127.0.0.1,localhost'
def buildjson (a):
	File = open ( a , 'r')
	file = File.read()
	jsonObject = json.loads(file)
    	File.close() ;
	return jsonObject

CRLF = "\r\n\r\n"

def download(a):
	jobj=buildjson(a)
	k=0
	entry=jobj['log']['entries']
	for i in entry :
		req=i['request']
		url=urlparse(req['url'])
		HOST=url.netloc
		path=url.path
		request=req['method']+"   "+path+" " + req['httpVersion']+"\r\n"
		#request='GET / HTTP /1.1'+ CRLF
		#for adding headers to request .
		for head in req['headers']:
			request+=head['name']+":"+head['value']+CRLF
		#print request
		key='connection'
		if key in i:
			PORT=int(i['connection'])
		else:
			PORT=80

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.connect((HOST, PORT))

		s.send(request)
		print "cool"
		result=""

		try:
			data=s.recv(1024)
			while len(data)>0 :
				result+=data
				data=s.recv(1024)


		except Exception as ex:
			pass
		print "recieved "
		filename="dump/"+HOST+path
		if path == "/":
			filename = "dump/"+HOST+".html"
		print "host "+HOST
		if not os.path.exists(os.path.dirname(filename)):
			os.makedirs(os.path.dirname(filename))
		print path
		# print filename
		f=open(filename,'w')
		pattern = '[C][o][n][t][e][n][t][-][T][y][p][e][:].*\r\n\r\n'
		x = re.split(pattern,result)
		print "length "+str(len(x))
		if(len(x) == 1):
			result=x[0]
		else :
			result=x[1]
		#for j in 1 to
		f.write(result.split("HTTP/1.")[0])
		#f.write(result)
		k+=1
		s.close()
		f.close()
		print "wrote"

#download(sys.argv[1])

def get(a,objectsPerConn):
	jobj=buildjson(a)
	entry=jobj['log']['entries']
	objectsPerConn = int(objectsPerConn)
	print len(entry)," cool"
	z = int(len(entry))/(objectsPerConn)
	i=0
	while i<z:
		socke = sock.mysocket()
		socke.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		j=0
		while j<objectsPerConn:
			print "cool ",i,j
			k = entry[i*objectsPerConn+j]
			req=k['request']
			url=urlparse(req['url'])
			HOST=url.netloc
			path=url.path
			request=req['method']+"   "+path+" " + req['httpVersion']+"\r\n"
			#request='GET / HTTP /1.1'+ CRLF
			#for adding headers to request .
			for head in req['headers']:
				request+=head['name']+":"+head['value']+CRLF
			key='connection'
			if key in k:
				PORT=int(k['connection'])
			else:
				PORT=80
			socke.connect(HOST,PORT)
			socke.mysend(request)
			print "bhenchod\n"
			result = socke.myreceive()
			filename="dump/"+HOST+path
			if path == "/":
				filename = "dump/"+HOST+".html"
			print "host "+HOST
			if not os.path.exists(os.path.dirname(filename)):
				os.makedirs(os.path.dirname(filename))
			print path
			# print filename
			f=open(filename,'w')
			pattern = '[C][o][n][t][e][n][t][-][T][y][p][e][:].*\r\n\r\n'
			x = re.split(pattern,result)
			print "length "+str(len(x))
			if(len(x) == 1):
				result=x[0]
			else :
				result=x[1]
			#for j in 1 to
			f.write(result.split("HTTP/1.")[0])
			#f.write(result)
			f.close()
			j+=1
			socke.sock.close()
		print z
		i+=1

get(sys.argv[1],sys.argv[2])
#download(sys.argv[1])
