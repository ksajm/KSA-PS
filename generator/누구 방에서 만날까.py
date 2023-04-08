import random

from genlib import ioData
from genlib import generate

dataList = []

inputDataList = [
    '435 439 437',
    '435 437 437',
    '435 435 435'
]

for testCase in range(100):
    numbers = [ str( random.randint(400, 500) ) for _ in range(3) ]
    inputStr = ' '.join(numbers)
    
    inputDataList.append(inputStr)

for inputStr in inputDataList:
    junee, changha, raehwan = inputStr.split()
    junee = int(junee)
    changha = int(changha)
    raehwan = int(raehwan)

    minRoom = min(junee, changha, raehwan)
    maxRoom = max(junee, changha, raehwan)

    if (junee == minRoom and changha == maxRoom) \
    or (changha == minRoom and junee == maxRoom):
        outputStr = '김래환'
    elif (raehwan == minRoom and changha == maxRoom) \
    or (changha == minRoom and raehwan == maxRoom):
        outputStr = '김준이'
    else:
        outputStr = '김창하'
    
    dataList.append( ioData(inputStr + '\n', outputStr) )

generate('누구 방에서 만날까', dataList)