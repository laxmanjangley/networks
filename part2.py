import os
import parser as p
import sys
#tree {node : parent} (tree I)
tree = {}
cTree = {}
pageloadTime = 0
nodeTree = {}
connect = {}
wait ={}
receive ={}
send ={}
startTime ={}
endTime = {}

# print tree
#connection ID :  parent
#connectionID : duration

#connectionID : list children
# 3 c iii 1
def connTree (ip):
	global cTree
	global tree
	global pageloadTime
	global nodeTree
	global connect
	global wait
	global receive
	global send
	global startTime
	global endTime
	file = 0
	fileName = 'connectionData/'
	commandTail = ' && http " -T fields -e tcp.stream  -e http.request.full_uri -e http.host >'
	commandHead = 'tshark -r nytimes.pcap -Y "ip.dst == '
	for i in ip:
		com = commandHead + i + commandTail + fileName + str(file)
		line = os.popen(com , "r")
		#print line
		#print com
		f = open(fileName + str(file) , 'r')
		line = f.readline()
		lis = line.split()
		#print 'a'
		link = 'manav'
		host = 'dude'
		while (line != ''):
			#print 2
			if(len(lis) == 3):
				link = lis[1]
				host = lis[2]
				conId = int(lis[0])
				# print 'here'
				if(not(conId in cTree)):
					cTree [conId] = host
					nodeTree[conId] = []
				if(not(link in nodeTree[conId])):
					nodeTree[conId].append(link)

				#3c iii 1- 4
				if(link in p.timings):
					for k in p.timings[link]:
						if(not(conId in connect)):
							# print k['connect']
							connect[conId] = k['connect']
						else:
							connect[conId] += k['connect']
						if(not(conId in wait)):
							wait[conId] = k['wait']
						else:
							wait[conId] += k['wait']
						if(not(conId in receive)):
							receive[conId] = k['receive']
						else:
							receive[conId] += k['receive']
						if(not(conId in send)):
							send[conId] = k['send']
						else:
							send[conId] += k['send']
						#3c iii 5 yes
						#3c iii 6 , 7 , 8 , 9 (experiment) , 11
						if(conId in startTime ):
							if (startTime[conId] > p.start[link] )	:
								startTime[conId] = p.start[link]
							if(endTime[conId] < p.end[link]):
								endTime[conId] = p.end[link]
						else:
							startTime[conId] = p.start[link]
							endTime[conId] = p.end[link]


			line = f.readline()
			lis = line.split()
		f.close()
		file =file + 1
	# print len(cTree) , len(nodeTree) , len(connect) , len(wait) , len(receive) , len(startTime) , len(endTime)

def reset(a):
	global cTree
	global tree
	global pageloadTime
	global nodeTree
	global connect
	global wait
	global receive
	global send
	global startTime
	global endTime

	# cTree = {}
	# nodeTree={}
	# connect = {}
	# wait ={}
	# receive ={}
	# send ={}
	# startTime ={}
	# endTime = {}
	# p.reset()
	tree , pageloadTime = p.buildTree (a)
	# print len(tree) , 'tree' , len (p.size) , len(p.ip)
	connTree (p.ip)
# reset(sys.argv[1])
# reset()
# print len(cTree) , len(nodeTree) , len(connect) , len(wait) , len(receive) , len(startTime) , len(endTime)
