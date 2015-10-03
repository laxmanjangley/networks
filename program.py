#!/usr/bin/python           

import socket               # Import socket module
import sys
import json
def buildjson (a):
	File = open ( a , 'r')
	file = File.read()
	jsonObject = json.loads(file)
    	File.close() ;
	return jsonObject
CRLF = "\r\n\r\n"
def download(a):
	jobj=buildjson(a)

	entry=jobj['log']['entries']
	for i in entry :
		req=i['request']
		request=req['method']+" "+req['url']+" " + req['httpVersion']
		
		#for adding headers to request .  
		#for head in req['headers']:
		#	request+=head['name']+":"+head['value']+CRLF
		print request
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(("www.nytimes.com", int(i['connection'])))
		s.send(request)
		result = s.recv(10000)
		print result
		while (len(result) > 0):
		    f=open(req['url'],'w')
		    f.write(result)
		    
		            
download(sys.argv[1])