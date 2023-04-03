# 유감

## 가장 보편적인 방법
```py
message = input()
if message == '이슈가 있는데?' or message == '이슈가 너무 큰데?':
    print('유감')
else:
    print('무감')
```

## in 연산자와 tuple 사용
```py
message = input()
if message in ('이슈가 있는데?', '이슈가 너무 큰데?'):
    print('유감')
else:
    print('무감')
```
---

# 이슈가 있는데?

## for에 string 넣기 <- 문제가 의도한 풀이
```py
def numberOfIssue(string):
    count = 0
    beforeChar = ''
    for char in string:
        if beforeChar == '이' and char == '슈':
            count += 1
        beforeChar = char
    return count

message = input()
## 메세지에 '이슈'라는 단어는 적어도 하나 반드시 존재함
if numberOfIssue(message) < 10:
    print('이슈가 있는데?')
else:
    print('이슈가 너무 큰데?')
```

## 파이썬 str 내장함수(메소드) 쓰기
```py
message = input()
## 메세지에 '이슈'라는 단어는 적어도 하나 반드시 존재함
if message.count('이슈') < 10:
    print('이슈가 있는데?')
else:
    print('이슈가 너무 큰데?')
```
---

# 아침 점호

## 의도한 풀이
```py
def fillTwoDigits(num):
    string = str(num)
    if len(string) == 1:
        return '0' + string
    else:
        return string
    
def getM(nameAndM):
    for mStartIndex in range(len(nameAndM), 0, -1):
        if nameAndM[ mStartIndex - 1 ] == ' ':
            break
    
    m = 0
    for char in nameAndM[ mStartIndex: ]:
        m *= 10
        m += int(char)
        
    return m

n = int(input())
sumOfM = 0

for numOfM in range(n):
    nameAndM = input()
    sumOfM += getM(nameAndM)

hours = fillTwoDigits( (8 * 60 - sumOfM) // 60 )
minutes = fillTwoDigits( (70 - sumOfM % 60) % 60 )
print(hours, minutes, sep = ':')
```

## split과 format 사용
```py
n = int(input())
sumOfM = 0

for numOfM in range(n):
    nameAndM = input().split()
    sumOfM += int( nameAndM[-1] )

hours = (8 * 60 - sumOfM) // 60
minutes = (70 - sumOfM % 60) % 60
print('{:02d}:{:02d}'.format(hours, minutes))
```
* split을 통해 띄어쓰기를 기준으로 구분하여 m을 구할 수 있다.
* format을 통해 시간과 분을 두 자리로 맞출 수 있다.
---

# 독감

## 의도한 풀이
```py
n, m = input().split()
n = int(n)
m = int(m)

infectedRooms = list(map(int, input().split()))
firstRoom = 422
lastRoom = 422 + n - 1

diffMax = infectedRooms[0] - (firstRoom - 1)

for i in range(1, m):
    diff = (infectedRooms[i] - infectedRooms[i - 1]) // 2
    if diffMax < diff:
        diffMax = diff

diff = (lastRoom + 1) - infectedRooms[-1]
if diffMax < diff:
    diffMax = diff

print(diffMax + 7)
```
* 두 방이 독감에 감염되었을 때, 두 방의 중앙에 위치한 방이 가장 마지막에 독감에 걸린다. 
* 양 끝에 위치한 방이 마지막에 독감에 걸리는지도 확인해야한다.