from urlparse import urlparse
import socket               # Import socket module
import sys
import json
import os
import re
import sock
import threading
import hashlib
import time

maxobj = sys.argv[3]

class connection (threading.Thread):
    def __init__(self, threadID, name, obj):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.obj = obj
    def run(self):
        print "Starting " + self.name
        threadfunction(self.name, self.obj, maxobj)
        print "Exiting " + self.name

CRLF = "\r\n\r\n"

def buildjson (a):
	File = open ( a , 'r')
	file = File.read()
	jsonObject = json.loads(file)
    	File.close() ;
	return jsonObject

def buildmap(b):
    entry = b['log']['entries']
    D={}
    for i in entry:
        #print i['serverIPAddress']
        if not (i['serverIPAddress'] in D):
            D[i['serverIPAddress']] = [i]
        else:
            D[i['serverIPAddress']].append(i)
    return D


def threadfunction(thread,val,objects):
    objectsleft = len(val)
    print objectsleft
    while objectsleft>0:
        j=0
        s = len(val)
        socke = sock.mysocket()
        socke.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        k = val[0]
        req=k['request']
        url=urlparse(req['url'])
        HOST=url.netloc
        path=url.path
        key='connection'
        if key in k:
        	PORT=int(k['connection'])
        else:
        	PORT=80
        #socke.connect(HOST,PORT)
        for l in range(s-objectsleft,s):
            i=val[l]
            j+=1
            if(j==objects):
                objectsleft-=j
                break
            if (l==s-1):
                objectsleft=0
            req=i['request']
            url=urlparse(req['url'])
            HOST=url.netloc
            path=url.path
            request=req['method']+"   "+path+" " + req['httpVersion']+"\r\n"
            for head in req['headers']:
                request+=head['name']+":"+head['value']+CRLF
            #socke.mysend(request)
            g=open("request",'w')
            g.write(request+"\n")
            result = socke.myreceive()
            filename="dump/"+HOST+path
            if path == "/":
            	filename = "dump/"+HOST+".html"
            if not os.path.exists(os.path.dirname(filename)):
            	os.makedirs(os.path.dirname(filename))
            f=open(filename,'w')
            f.write(result)
            pattern = '[C][o][n][t][e][n][t][-][T][y][p][e][:].*\r\n\r\n'
            x = re.split(pattern,result)
            if(len(x) == 1):
            	result=x[0]
            else :
            	result=x[1]
            print result.split("HTTP/1.")[0]
            f.write(result.split("HTTP/1.")[0])
            f.close()
        socke.sock.close()

def downloader(a,connections,objects):
    jobj = buildjson(a)
    m = buildmap(jobj)
    if (connections*objects < len(jobj['log']['entries'])):
        print "Please provide proper inputs"
        return -1
    j=0
    T=[]
    for i in m:
        j+=1
        T.append(connection(j,"thread "+str(j),m[i]))
        T[j-1].start()


downloader(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
