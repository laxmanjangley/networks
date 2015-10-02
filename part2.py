import os
import parser as p
import sys
tree = p.buildTree (sys.argv[1])

def connTree (ip):
	file = 0
	fileName = 'connectionData/'
	commandTail = ' && http " -T fields -e tcp.stream  >'
	commandHead = 'tshark -r nytimes.pcap -Y "ip.dst == '
	for i in ip:
		com = commandHead + i + commandTail + fileName + str(file)
		file =file + 1
		line = os.popen(com , "r")
		#print line		
		#print com
	
	
connTree (p.ip)




