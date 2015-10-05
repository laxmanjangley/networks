import json
import sys
import unicodedata

def buildjson (a):
	File = open ( a , 'r')
	file = File.read()
	jsonObject = json.loads(file)
    	File.close() ;
	return jsonObject
types = []
size = {}
ip = {}
timings = {}
dnsTime = {}
start = {}
end = {}
#return tree , page load time
def buildTree (a):
	# pageloadTime = 0
	startTime = 100000000
	endTime = 0
	jsonObject = buildjson(a)
	tree = {}
	entries = jsonObject['log']['entries']
	for i in entries:
		curr = i['request']['url']
		x = ''
		# ...
		if (curr in timings):
			timings[curr].append(i['timings'])
		else :
			timings[curr] = [i['timings']]
		#3 c i
		sdt = unicodedata.normalize('NFKD' , i['startedDateTime']).encode('ascii' , 'ignore')
		if(len(sdt) > 21):
			sdt = sdt[11:23]
			l = sdt.split(':')
			# print 'time-' , l
			start[curr] = 3600*float(l[0])+ 60*float(l[1]) + float(l[2])
			end[curr] = start[curr] + i['time']
			if(startTime > start[curr] ): startTime = start[curr]
			if(endTime < end[curr]): endTime = end[curr]


		# 3 c ii
		if(not(curr in dnsTime)) :
			dnsTime[curr] = i['timings']['dns']

		if(not(curr in tree)):
			for j in i['request']['headers']:
				if(j['name'] == 'Referer'):
					tree[curr] = j['value']
					# if(not(i['serverIPAddress'] in ip)):
					ip[i['serverIPAddress']] = j['value']
						# ipReqUrl[i[server]] = [curr]
					# else:
					# 	ip[i['serverIPAddress']].append( j['value'])
						# ipReqUrl[i['serverIPAddress']].append( curr)
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
	# print startTime - endTime
	# print ip
	return tree , endTime - startTime
def reset():
	types =[]
	ip = {}
	size = {}
	dnsTime = {}
