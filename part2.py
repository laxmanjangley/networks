import os
import parser as p
import sys
#tree {node : parent} (tree I)
tree = p.buildTree (sys.argv[1])
#connection ID :  parent
cTree = {}
#connectionID : list children
nodeTree = {}

def connTree (ip):
	file = 0
	fileName = 'connectionData/'
	commandTail = ' && http " -T fields -e tcp.stream  -e http.request.full_uri>'
	commandHead = 'tshark -r nytimes.pcap -Y "ip.dst == '
	for i in ip:
		com = commandHead + i + commandTail + fileName + str(file)
		line = os.popen(com , "r")
		#print line
		#print com
		f = open(fileName + str(file) , 'r')
		line = f.readline()
		while (line != ''):
			lis = line.split()
			conId = int(lis[0])
			if(not(conId in cTree)):
				cTree [conId] = ip[i]
				nodeTree[conId] = []
			if (len(lis) == 2):
				if(not(lis[1] in nodeTree[conId])):
					nodeTree[conId].append(lis[1])
			line = f.readline()
		f.close()
		file =file + 1

def reset():
	cTree = {}
	nodeTree={}
	
connTree (p.ip)
