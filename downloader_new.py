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
        self.stt = False
        self.objectstaken = 0
        self.name = name
        self.request = ""
        self.HOST = ""
        self.path = ""
        self.connect = connect
        self.socke = sock.mysocket()
        self.socke.connect(connect[0],connect[1])
    def run(self):
        if not(self.request==''):
            print "retreiving "+self.HOST+self.path
            self.objectstaken +=1
            self.socke.mysend(self.request)
            result = self.socke.myreceive()
            while (result == ""):
                self.socke.sock.close()
                self.socke =sock.mysocket()
                self.socke.connect(self.connect[0],self.connect[1])
                self.socke.mysend(self.request)
                result = self.socke.myreceive()
            filename="dump/"+self.HOST+self.path
            if filename[len(filename)-1] == '/':
                filename = "dump/"+self.HOST+".html"
            if not os.path.exists(os.path.dirname(filename)):
                os.makedirs(os.path.dirname(filename))
            print filename
            f=open(filename,'w')
            f.write(result)
            pattern = '\r\n\r\n'
            x = re.split(pattern,result)
          #  print len(x)
           # print  "jdjdjdjdjd\n"
            x=x[1:]
            result="".join(x)
            f.write(result)
            f.close()
            if(self.objectstaken==int(sys.argv[3])):
                self.objectstaken = 0
            self.request=''

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
        R = {}
        for e in range(0,len(M)):
            I=m[i][e]
            req=I['request']
            url=urlparse(req['url'])
            HOST=url.netloc
           # print HOST,I['connection']
            path=url.path
           # print path
            request=req['method']+"   "+path+" " + req['httpVersion']+"\n"
            for head in req['headers']:
                if (head['name'] == 'Host'):
                    request+=head['name']+":"+head['value']+"\n\n"
            R[request] = True
                # else:
                #     request+=head['name']+":"+head['value']+"\n\n"
            while(R[request]==True):
                for t in range(0,len(T[i])):
                    if (not(T[i][t].isAlive()) and (T[i][t].objectstaken<objects) and (R[request]==True)):
                        T[i][t].request = request
                        T[i][t].HOST = HOST
                        T[i][t].path = path
                        T[i][t].run()
                        # if (T[i][t].stt == False):
                        #     T[i][t].start()
                        #     T[i][t].stt = True
                        R[request] = False
                        t = len(T[i])
    for i in T:
        for j in range(0,len(T[i])):
            T[i][j].socke.sock.close()


downloader(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
