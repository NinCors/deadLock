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


#check if all the process finished
def checkFinish():
    for i in finishInfo:
        if i != True:
            return False
    return True

# check if request<avaiable
def checkAvailable(requestN):
    for i in range(resourceNum):
        if int(requestInfo[requestN][i]) > int(availableInfo[i]):
            return False
    return True

# update available status
def updateAvailable(processN):
    global availableInfo
    global allocationInfo
    for i in range(resourceNum):
        availableInfo[i] = int(availableInfo[i]) + int(allocationInfo[processN][i])
        allocationInfo[processN][i] = 0

#dead lock detecter
def dlDetecter():
    global finishInfo

    end = False

    count = 0
    while end == False:
        find = False
        for i in range(processNum):
            if finishInfo[i] == False:
                print('\n')
                print('For process %d '%(i))
                print('Request is ')
                print(requestInfo[i])
                print('Available resource is ')
                print(availableInfo)
                if checkAvailable(i):
                    count=count+1
                    updateAvailable(i)
                    finishInfo[i] = True
                    find =True

        if find == False and checkFinish() == False:
            print('\nDead lock process are ')
            for p in range(len(finishInfo)):
                if finishInfo[p] == False:
                    print('Process: %d'%(p+1))
            end = True

        elif checkFinish():
            print('\nAll finished!')
            end = True
        

def runner():
    if len(sys.argv) != 2:
        print("Wrong Input file")
        exit()
    #Get all the data from file
    getData()
    dlDetecter()
    

runner()
