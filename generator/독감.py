import random

from genlib import ioData
from genlib import generate

dataList = []

inputDataList = [
    '4 1\n424\n',
    '6 2\n424 428\n',
    '1 1\n423\n'
]

for testCase in range(100):
    n = random.randint(1, 50)
    m = random.randint(1, n + 1)
    rooms = [r + 423 for r in range(m)]
    random.shuffle(rooms)

    inputStr = f'{n} {m}\n'
    for i in range(m):
        inputStr += f'{rooms.pop()} '
    inputStr = inputStr[:-1]
    inputStr += '\n'

    inputDataList.append(inputStr)

for inputStr in inputDataList:
    n, m = inputStr.split('\n')[0].split()
    n = int(n)
    m = int(m)

    infectedRooms = list(map(int, inputStr.split('\n')[1].split()))
    firstRoom = 423
    lastRoom = 423 + n - 1

    maxDiff = infectedRooms[0] - firstRoom

    for i in range(1, m):
        diff = (infectedRooms[i] - infectedRooms[i - 1]) // 2
        if maxDiff < diff:
            maxDiff = diff

    diff = lastRoom - infectedRooms[-1]
    if maxDiff < diff:
        maxDiff = diff

    outputStr = maxDiff + 8
    
    dataList.append( ioData(inputStr, outputStr) )

generate('독감', dataList)