import part2 as p2
import sys
import os
import json

p2.reset(sys.argv[1] , sys.argv[2])
d = os.path.dirname(sys.argv[3]+'/')
if not os.path.exists(d):
    os.mkdir(d)

print 'here'  , len(p2.tree) , 'X' , len(p2.nodeTree)
objects = len(p2.tree)
totalSize = 0
downOnEachDomain = {}
sizeOnEachDomain = {}

# f = open('3_a_i' , "w")
#3 a i
for i in p2.tree:
    # print i
    if(p2.tree[i] in downOnEachDomain):
        # print 'here'
        downOnEachDomain[p2.tree[i]] += 1
        sizeOnEachDomain[p2.tree[i]] += p2.p.size[i]
    else:
        # print 'tgs'
        downOnEachDomain[p2.tree[i]] = 1
        sizeOnEachDomain[p2.tree[i]] = p2.p.size[i]
    totalSize += p2.p.size[i]
d = os.path.dirname(sys.argv[3]+'/3_a/')
if not os.path.exists(d):
    os.mkdir(d)
f1 = open(sys.argv[3]+'/'+'3_a/i_ii.csv' , "w")
line = 'domain , noOfDownloads , sizeDownloaded \n'
f1.write(line)
for i in downOnEachDomain:
    line = i + ' , ' + str(downOnEachDomain[i] ) + ' , ' + str(sizeOnEachDomain[i])  +' \n'
    f1.write(line)
f1.close()
f1 = open(sys.argv[3]+'/'+'3_a/types.txt' , "w")
f1.write( 'total types = ' + str(len (p2.p.types))+ '\n' + '\n'.join(p2.p.types) + '\n')
f1.close()

f1 = open(sys.argv[3]+'/'+'3_a/iv.csv' , "w")
line = 'Domain , noOfTcpConnection'
for i in range(0,20):
    line += ' , ' + str(i)
line += '\n'
nc = {}
for i in p2.cTree:
    if(p2.cTree[i] in nc):
        nc[p2.cTree[i]].append(i)
    else:
        nc[p2.cTree[i]] = [i]
f1.write(line)
print len(nc) , 'qwe'
for i in nc:
    line = i + ' , ' +str(len(nc[i]))
    for j in nc[i]:
        line +=  ' , ' + str(len(p2.nodeTree[j]))
    line += '\n'
    f1.write(line)
f1.close()

d = os.path.dirname(sys.argv[3]+'/'+'3_b/')
if not os.path.exists(d):
    os.mkdir(d)
f1 = open(sys.argv[3]+'/'+'3_b/downloadTree.txt' , "w")
for i in nc:
    line = 'parent =' + i + '\n'
    f1.write(line)
    for k in nc[i]:
        line =  '\t\tconnectionID = ' + str(k) +'\n'
        f1.write(line)
        for j in p2.nodeTree[k]:
            line = '\t\t\t\t' +j + '\n'
            f1.write(line)
f1.close()

pt = {}
for i in p2.tree:
    if(p2.tree[i] in pt):
        pt[p2.tree[i]].append(i)
    else:
        pt[p2.tree[i]] = [i]

f1 = open(sys.argv[3]+'/'+'3_b/objectTree', "w")
for i in pt:
    line = 'parent : ' + i + '\nchildren\n'
    for j in pt[i]:
        line += '\t\t'+j + '\n'
    line += '\n\n'
    f1.write(line)
f1.close()

d = os.path.dirname(sys.argv[3]+'/'+'3_c/')
if not os.path.exists(d):
    os.mkdir(d)
f1 = open(sys.argv[3]+'/'+'3_c/i_and_ii' , "w")
f1.write('pageloadTime =' + str (p2.pageloadTime)+ '\n')
for i in p2.p.dnsTime:
    if(not p2.p.dnsTime[i] == 0):
        line = i + '= ' + str(p2.p.dnsTime[i])+ '\n'
        f1.write(line)
f1.write('\n\n All othere dns resolution time is 0.')
f1.close()

data = {}
maxdata = {}
rtime = {}
avgoodput = {}
for i in p2.nodeTree:
    maxdata[i] = 0
    rtime[i] = 1.0
    ii = 0.0
    for j in p2.nodeTree[i]:
        if(i in data):
            if j in p2.p.size :
                data[i] += p2.p.size[j]
        elif(j in p2.p.size) :
            data[i] = p2.p.size[j]
        if( j in p2.p.size):
            if(maxdata[i] < p2.p.size[j]):
                maxdata[i] = p2.p.size[j]
                if(i in p2.p.timings):
                    for k in p2.p.timings[i]:
                        # print k
                        rtime[i] += k['receive']
        ii += 1.0
# d = os.path.dirname('3_c/iii')
# os.mkdir(d)
#5 10 11 todo
f2 = open(sys.argv[3]+'/'+'3_c/iii.csv' , "w")
f2.write('TCP , Connect , Wait , Receive , Send , totalTime , ActivePercentage , AverageGoodput , maxGoodPut  \n')
# maxgoodput = 0 ; d = 0 ;
# print 'asd'
totalAvgput = 0
maxgp = 0
y = 0.0
for i in p2.connect:
    x = 1.0
    y += 1.0
    if(not p2.receive[i] == 0.0):
        x = p2.receive[i]
    line = str(i)+ ',' + str(p2.connect[i])+ ',' +str(p2.wait[i])+ ',' +str(p2.receive[i])+ ',' +str(p2.send[i])+ ','
    line += str( p2.endTime[i] - p2.startTime[i])+ ',' +str((p2.send[i] + p2.wait[i] + p2.receive[i]) / ( p2.endTime[i] -p2.startTime[i] )) +','
    line += str(data[i] /x ) +','+str(maxdata[i] / rtime[i]) + '\n'#str(data[i] / rtime[i])+
    f2.write(line)
    totalAvgput = data[i] /x
    if (maxgp< maxdata[i] / rtime[i]):
        maxgp = maxdata[i] / rtime[i]

f2.close()
totalAvgput /= y
f2 = open(sys.argv[3]+'/'+'3_c/X_XI' , "w")
f2.write('Average achieved goodput = '+ str(totalAvgput) + '\n')
if(totalAvgput < maxgp):
    f2.write( ' No , browser didnt utilised resources efficiently,\n as we can say by analyzing :\n\t\t total average goodput < overall max goodput ')
else:
    f2.write( ' Yes , browser didnt utilised resources efficiently,\n as we can say by analyzing :\n\t\t total average goodput = overall max goodput ')
f2.close()


##url :no

simCon = {}
intersection = {}
for i in nc:
    ma = {}
    for j in nc[i] :
        for k in nc[i] :
            if j in p2.startTime and k in p2.startTime:
                if p2.startTime[j] <= p2.startTime[k] < p2.endTime[j] or p2.startTime[j] < p2.endTime[k] <= p2.endTime[j]:
                    if j in ma:
                        ma[j] += 1
                    else:
                        ma[j] = 1
            # else:
            #     print 'skipped'
    simCon[i] =  0
    for j in ma:
        if(simCon[i] < ma[j]):
            simCon[i] = ma[j]
    if simCon[i] == 0:
        simCon[i] =1

f3 = open (sys.argv[3]+'/'+'3_c/iv.csv' , "w")
# print simCon , len(simCon)
f3.write('Domain , noOfTCPsOpened , simultanousConnectionOpened \n')
for i in nc :
        f3.write(i +','+ str(len(nc[i]))+ ','+str(simCon[i]) + '\n') # ','+str(simCon[i])
f3.close()
