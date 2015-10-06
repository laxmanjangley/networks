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
    def __init__(self, threadID, name, connect):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.objectstaken = 0
        self.name = name
        self.connect = connect
        self.socke = sock.mysocket()
        self.socke.connect(connect[0],connect[1])
    def run(self,request,HOST,path):
        self.objectstaken +=1
        self.socke.mysend(request)
        result = self.socke.myreceive()
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
        req=i['request']
        url=urlparse(req['url'])
        HOST=url.netloc
        key='connection'
        if key in i:
        	PORT=int(i['connection'])
        else:
        	PORT=80
        if not ((HOST,PORT) in D):
            D[(HOST,PORT)] = [i]
        else:
            D[(HOST,PORT)].append(i)
    return D


def downloader(a,connections,objects):
    jobj = buildjson(a)
    m = buildmap(jobj)
    j=0
    T={}
    for i in m:
        T[i] = []
        for k in range(0,connections):
            j+=1
            T[i].append(connection(j,"thread "+str(j),i))
        M = m[i]
        for e in range(0,len(M)):
            I=m[i][e]
            req=I['request']
            url=urlparse(req['url'])
            HOST=url.netloc
            path=url.path
            request=req['method']+"   "+path+" " + req['httpVersion']+"\r\n"
            for head in req['headers']:
                if (head['name'] == 'Host'):
                    request+=head['name']+":"+head['value']+"\r\n"
                else:
                    request+=head['name']+":"+head['value']+CRLF
            for t in range(0,len(T[i])):
                if (not(T[i][t].isAlive()) and (T[i][t].objectstaken<objects)):
                    T[i][t].run(request,HOST,path)
    for i in T:
        for j in range(0,len(T[i])):
            T[i][j].socke.sock.close()


downloader(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
