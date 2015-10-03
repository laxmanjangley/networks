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

dnsTime = {}

#return tree , page load time
def buildTree (a):
	pageloadTime = 0
	jsonObject = buildjson(a)
	tree = {}
	entries = jsonObject['log']['entries']
	for i in entries:
		curr = i['request']['url']
		x = ''
		#3 c i
		pageloadTime += i['time']
		# 3 c ii
		if(not(curr in dnsTime)) :
			dnsTime[curr] = i['timings']['dns']

		if(not(curr in tree)):
			for j in i['request']['headers']:
				if(j['name'] == 'Referer'):
					tree[curr] = j['value']
					if(not(i['serverIPAddress'] in ip)):
						ip[i['serverIPAddress']] =j['value'] 
		if(not(curr in size)):
			size[curr] = i['response']['bodySize']
		elif(i['response']['bodySize'] > 0):
			size[curr] +=i['response']['bodySize']

		# types
		for j in range(len(curr) - 5 , len(curr)-1 ):
			if(curr[j] == '.'):
				x = curr[j:]
				break
		if(not (x in types or x == '')):
			types.append(x)
	# print pageloadTime
	#print dnsTime
	return tree , pageloadTime
def reset():
	types =[]
	ip = {}
	size = {}
	dnsTime = {}
