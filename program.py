#!/usr/bin/python           

#proxy pe nahi chalega. 

from urlparse import urlparse 
import socket               # Import socket module
import sys
import json
import os

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
				print data
				data=s.recv(1024)

				
		except Exception as ex: 
			pass
		print "recieved "
		f=open(str(k),'w')
		f.write(result)
		k+=1
		s.close()
		f.close()
		print "wrote"	
		            
download(sys.argv[1])