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
y = 0
def buildTree (a):
	jsonObject = buildjson(a)
	tree = {}
	entries = jsonObject['log']['entries']
	for i in entries:
		curr = i['request']['url']
		x = ''
		if(not(curr in tree)):
			for j in i['request']['headers']:
				if(j['name'] == 'Referer'):
					tree[curr] = j['value']
		if(not(curr in size)):
			size[curr] = i['response']['bodySize']
		elif(i['response']['bodySize'] > 0):
			size[curr] +=i['response']['bodySize']
		for j in range(len(curr) - 5 , len(curr)-1 ):
			if(curr[j] == '.'):
				x = curr[j:]
				break
		if(not (x in types or x == '')):
			types.append(x)
	return tree
def reset():
	types =[]
	ip = {}
	size = {}
