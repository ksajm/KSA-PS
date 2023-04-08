# genlib 사용법

## 기본 문법

```py
# generator python file은 generator 폴더에만 만듦
from .genlib import ioData
from .genlib import generate

# fileName is str and data is list of ioData
generate(fileName, dataList)
```

## ioData 형식

```py
from .genlib import ioData

data1 = ioData(inputStr, outputStr)
# data1.input == inputStr
# data2.output == outputStr
```

## example

### 기본

```py
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
```

### 랜덤 gen

```py
import random

from genlib import ioData
from genlib import generate

dataList = []

inputDataList = [
    '이 슈크림빵은 맛에 이슈가 있다.',
    '이슈 + 이슈 + 이슈 + 이슈 + 이슈 + 이슈 + 이슈 + 이슈 + 이슈 + 이슈 = 이십슈',
    '슈 이슈1이슈2이슈3이슈4이슈5이슈6이슈7이슈8이슈9 (민겸이를 위한 예제) 이'
]

words = ['이', '슈', '이슈', '이슈', '이슈 ', '이슈 ', '이슈 ', '이슈가 ', '앙기모띠 ', '김래환 바보 ', '김창하 바보 ', '헉 ', '김준이 천재 ']
for testCase in range(100):
    moreInput = ''
    for wordCount in range(random.randint(3, 30)):
        moreInput += random.choice(words)
    if '이슈' in moreInput:
        inputDataList.append(moreInput)

for inputStr in inputDataList:
    if inputStr.count('이슈') < 10:
        outputStr = '이슈가 있는데?'
    else:
        outputStr = '이슈가 너무 큰데?'
    dataList.append( ioData(inputStr, outputStr) )

generate('이슈가 있는데', dataList)
```