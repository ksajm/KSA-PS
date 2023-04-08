import random

from genlib import ioData
from genlib import generate

dataList = []

inputDataList = [ '4\n씻기 10\n옷 입기 1\n엘리베이터 기다리기 2\n세탁물 맡기기 3\n' ]

for testCase in range(100):
    works = [
        [ '씻기', random.randint(5, 20) ],
        [ '옷 입기', random.randint(1, 5) ],
        [ '밥 먹기', random.randint(10, 20) ],
        [ '래환이 깨우기', 1 ],
        [ '유튜브 보기', random.randint(1, 11) ],
        [ '세탁물 맡기기', random.randint(1, 4) ],
        [ '면도하기', 1 ],
        [ '세미나실 예약하기', random.randint(1, 4) ],
        [ '예습하기', random.randint(1, 30) ],
        [ '아침 태권도 하기', 30 ]
    ]

    workNum = random.randint(1, len(works))
    inputStr = f'{workNum}\n'
    random.shuffle(works)

    for i in range(workNum):
        work = works.pop()
        inputStr += f'{work[0]} {work[1]}\n'

    inputDataList.append(inputStr)

for inputStr in inputDataList:
    n = int(inputStr.split('\n')[0])
    sumOfM = 0

    for numOfM in range(1, n + 1):
        nameAndM = inputStr.split('\n')[numOfM].split()
        sumOfM += int( nameAndM[-1] )

    hours = (8 * 60 - sumOfM) // 60
    minutes = (70 - sumOfM % 60) % 60
    outputStr = '{:02d}:{:02d}'.format(hours, minutes)
        
    dataList.append( ioData(inputStr, outputStr) )

generate('아침 점호', dataList)