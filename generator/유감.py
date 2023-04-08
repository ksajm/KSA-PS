from genlib import ioData
from genlib import generate

dataList = []

inputDataList = [
    '이슈가 있는데?',
    '이슈가 너무 큰데?',
    '이슈가 없는데?',
    '삼슈가 있는데?',
    '이슈가 있는데',
    '이슈가 너무 큰데'
]

for inputStr in inputDataList:
    if inputStr in ['이슈가 있는데?', '이슈가 너무 큰데?']:
        outputStr = '유감'
    else:
        outputStr = '무감'
        
    dataList.append( ioData(inputStr, outputStr) )

generate('유감', dataList)