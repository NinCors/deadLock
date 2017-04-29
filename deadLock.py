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

    global availableInfo
    availableInfo = allInfo[2]

    global allocationInfo
    global finishInfo
    for i in range(3,3 + processNum):
        allocationInfo.append(allInfo[i])
        finishInfo.append(False);

    global requestInfo
    for w in range(3 + processNum, 3 + 2*processNum):
        requestInfo.append(allInfo[w])

    printInfo()

def printInfo():
    print('ProcessNum: %d\n'%(processNum))
    print('resourceNum: %d\n'%(resourceNum))
    print('Available resource is ')
    print( availableInfo )
    print('Allocation matrix is ')
    print(allocationInfo)
    print('Request matrix is ')
    print(requestInfo)
    print('Finish status is ')
    print(finishInfo)


#check if the matrix is 0
def checkFinish(matrix):
    for i in matrix:
        if i != '0':
            return False
    return True

# check if request<avaiable
def checkAvailable(request):
    for i in range(resourceNum):
        if int(request[i]) > int(availableInfo[i]):
            return False
    return True

# update finish status
def updateFinish():
    global finishInfo
    for i in range(resourceNum):
        finishInfo[i] = checkFinish(allocationInfo[i])

# update available status
def updateAvailable(allocation):
    global availableInfo
    for i in range(resourceNum):
        availableInfo[i] = int(availableInfo[i]) + allocation[i]

#dead lock detecter
def dlDetecter():
    # update finish status first
    updateFinish()
    
    for i in range(processNum):
        if finishInfo[i] == False and checkAvailable(requestInfo[i]):
            updateAvailable(allocationInfo[i])


def runner():
    if len(sys.argv) != 2:
        print("Wrong Input file")
        exit()
    #Get all the data from file
    getData()
    

runner()
