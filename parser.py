import json
import sys


def buildjson (a):
	File = open ( a , 'r')
	file = File.read()
	jsonObject = json.loads(file)
    	File.close() ;
	return jsonObject
types = []
size = {} 
ip = {}
def buildTree (a):
    jsonObject = buildjson(a)
    tree = {}
    entries = jsonObject['log']['entries']
    for i in entries:
        curr = i['request']['url']
	x= ''
	if(not (curr in tree)):
		for j in i['request']['headers']:
		    if(j['name'] == 'Referer' ):
		    	tree[curr] =  j['value'] 
			ip[i['serverIPAddress']] = curr			
	if((not (curr in size)) and  (i['response']['bodySize'] > 0 )):
		size[curr] = i['response']['bodySize']
	elif (i['response']['bodySize'] > 0):
		size[curr] += i['response']['bodySize']
	for j in range(len(curr) -1 , len(curr) - 5 , -1):
		if (curr[j] == '.'):
			x = curr[j:]
			break
	if(not(x in types) and  (not(x==''))):
		types.append(x)	
    return tree
def reset():
	types =[]
	ip = {}
	size = {}
#tree =  buildTree (sys.argv[1])
#noOfObjects = len (tree)
#print types
#print size

