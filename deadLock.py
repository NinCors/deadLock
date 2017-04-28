import sys
import os

processNum = 0
resourceNum = 0

availableInfo = []
allocationInfo = []
requestInfo = []
finishInfo = []

def getData():
    file_path = os.getcwd() + "/" + sys.argv[1]
    allInfo = []
    try:
        with open(file_path,'rb') as file:
            for line in file:
                d = line.split()
                allInfo.append(d)
    except IOError as msg:
        msg = "\n '{0}' cannot be read : {1} \n".format(file_path,msg)
        print(msg)
        exit()
    
    global processNum 
    processNum = int(allInfo[0][0])
   
    global resourceNum
    resourceNum= int(allInfo[1][0])

    for i in range(3,3 + processNum):
        allocationInfo.append(allInfo[i])

    for w in range(3 + processNum, 3 + 2*processNum):
        requestInfo.append(allInfo[w])
    
    printInfo()

def printInfo():
    print('ProcessNum: %d\n'%(processNum))
    print('resourceNum: %d\n'%(resourceNum))
    print('Allocation matrix is \n')
    print(allocationInfo)
    print('Request matrix is \n')
    print(requestInfo)

getData()
