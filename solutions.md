* [문제 보기](./problems.md)

---

# 유감

## 설명
조건문을 잘 이해하고 있는지 확인하는 문제이다.

## 가장 보편적인 방법

```py
message = input()
if message == '이슈가 있는데?' or message == '이슈가 너무 큰데?':
    print('유감')
else:
    print('무감')
```

## in 연산자와 tuple 사용
* [in 연산자](https://velog.io/@binsu/Python-%EB%AC%B8%EB%B2%95-in-not-in-%EC%97%B0%EC%82%B0%EC%9E%90)

```py
message = input()
if message in ('이슈가 있는데?', '이슈가 너무 큰데?'):
    print('유감')
else:
    print('무감')
```

---

# 누구 방에서 만날까?

## 설명
최소 에너지를 사용하는 방법을 생각해야 한다. 양 끝 방에 위치한 사람들이 소모하는 에너지의 합은 동일하므로 가운데 위치한 방에서 만나는 것이 답이다. 3명중 여러 명이 한 방에 있을 수도 있다는 점을 주의해야한다.

## 가운데 수 조건문으로 찾기

```py
junee, changha, raehwan = input().split()
junee = int(junee)
changha = int(changha)
raehwan = int(raehwan)

minRoom = min(junee, changha, raehwan)
maxRoom = max(junee, changha, raehwan)

if (junee == minRoom and changha == maxRoom) \
or (changha == minRoom and junee == maxRoom):
    print('김래환')
elif (raehwan == minRoom and changha == maxRoom) \
or (changha == minRoom and raehwan == maxRoom):
    print('김준이')
else:
    print('김창하')
```

## dict와 sorted 사용
* [dict](https://wikidocs.net/16043)
* [dict sort by value](https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/)
* [lambda](http://www.gisdeveloper.co.kr/?p=9031)

```py
r1, r2, r3 = map(int, input().split())

rooms = {
    '김준이': r1,
    '김창하': r2,
    '김래환': r3
}

rooms = sorted(rooms.items(), key = lambda x:x[1])
print(rooms[1][0])
```

---

# 이슈가 있는데?

## 설명
하나의 긴 문자열에서 특정 문자열을 어떻게 찾는지, 그리고 그 개수를 어떻게 찾을지 생각해야 한다.

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
* [count 메소드](https://www.entity.co.kr/entry/43-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%AC%B8%EC%9E%90%EC%97%B4-count-%EB%A9%94%EC%86%8C%EB%93%9C)

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

## 설명
이 문제는 하나의 큰 기능을 여러 개의 작은 기능들로 나누어 코드를 작성할 수 있는지 확인하는 문제이다. 다음과 같이 구현할 기능들을 나누어 문제에 적용하면 쉽게 풀 수 있다.

* 할 일 이름과 걸리는 시간: 마지막 띄어쓰기를 기준으로 구분한다.
* 시간 차이를 계산: 시간/분의 60진법과 받아내림을 생각하며 식을 세운다.
* 자릿수 채우기: 각 시간과 분의 자릿수를 확인하고 이를 채운다.

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

* 기능 별로 함수를 만들어 문제에 필요한 각 기능들을 구별한다.

## split과 format 사용
* [split](https://www.entity.co.kr/entry/47-Python-%EB%AC%B8%EC%9E%90%EC%97%B4-split-%EB%AA%A9%EB%A1%9D-%EB%AC%B8%EC%9E%90%EB%B3%84-%EA%B5%AC%EB%B6%84-%EA%B8%B0%ED%98%B8)
* [format](https://ddolcat.tistory.com/692)

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

## 설명
독감이 어떻게 확산되는지 알아내야 한다. 헷갈린다면 직접 그림이나 표를 그려 확인하는 것도 좋은 방법이다. 두 방이 독감에 감염되었을 때, 두 방의 중앙에 위치한 방이 가장 마지막에 독감에 걸린다. 마지막에 독감에 걸리는 시점이 중요하기 때문에, (최초 감염된 방들 사이 거리)/2를 비교하여 그 시점을 구한다. 이 때, 양 끝에 위치한 방이 마지막에 독감에 걸릴 수 있음을 유의 해야 한다.

## 의도한 풀이

```py
n, m = input().split()
n = int(n)
m = int(m)

infectedRooms = list(map(int, input().split()))
firstRoom = 422
lastRoom = 422 + n - 1

maxDiff = infectedRooms[0] - firstRoom

for i in range(1, m):
    diff = (infectedRooms[i] - infectedRooms[i - 1]) // 2
    if maxDiff < diff:
        maxDiff = diff

diff = lastRoom - infectedRooms[-1]
if maxDiff < diff:
    maxDiff = diff

print(maxDiff + 8)
```

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n, m, maxval = -1, past, room;
    cin >> n >> m;
    for(int i = 0; i < m; i++)
    {
        cin >> room;
        if (i == 0)
        {
            maxval = max(maxval, room - 423);
        }
        else
        {
            maxval = max(maxval, (room - past) / 2);
        }
        past = room;
    }
    maxval = max(maxval, 423 + n - 1 - room);
    cout << maxval + 8;
}
```

---

# 마인크래프트 1

## 설명
그래프에서 두 정점 사이 거리를 구하는 알고리즘을 생각해야 한다. 한 칸 이동하는데 걸리는 시간이 1초로 같으므로, BFS를 사용하면 쉽게 풀 수 있다.

## BFS (너비 우선 탐색)
* [BFS](https://namu.wiki/w/%EB%84%88%EB%B9%84%20%EC%9A%B0%EC%84%A0%20%ED%83%90%EC%83%89)

```py
w, h = map(int, input().split())
location = []
direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
queue = []
hasAnswer = False


def getInput():
    for i in range(h):
        location.append(list(
            map(int, input().split())
        ))

def isInRange(x, y):
    return 0 <= x < w and 0 <= y < h

def checkNextBlock(arg):
    global hasAnswer
    x, y, dis = arg

    for move in direction:
        nextX = x + move[0]
        nextY = y + move[1]
        if not isInRange(nextX, nextY):
            continue

        if location[nextY][nextX] == -1:
            hasAnswer = True
            print(dis + 1)
            return
        elif location[nextY][nextX] != -2:
            location[nextY][nextX] = -2
            queue.append((nextX, nextY, dis + 1))

def startBFS():
    for i in range(h):
        for j in range(w):
            if location[i][j] == -1:
                location[i][j] = -2
                checkNextBlock((i, j, 0))
                return


getInput()
startBFS()

while len(queue) >= 0 and not hasAnswer:
    checkNextBlock(queue.pop(0))
```

* queue에 x, y, 거리를 튜플로 담아 checkNextBlock의 인자로 넘겼다. 

```cpp
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

queue<int> qx, qy;
int dirx[4] = { 0, 1, 0, -1 }, diry[4] = { 1, 0, -1, 0 };

int main()
{
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);
    int f[64][64], visited[64][64] = { 0, };
    int w, h;
    cin >> w >> h;
    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            cin >> f[i][j];
        }
    }

    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            if (f[i][j] == -1)
            {
                int size = 1, dist = 0;
                qx.push(j), qy.push(i);
                while (!qx.empty())
                {
                    int herex = qx.front(), herey = qy.front();
                    visited[herey][herex] = 1;
                    for (int i = 0; i < 4; i++)
                    {
                        int therex = herex + dirx[i], therey = herey + diry[i];
                        if (therex >= 0 && therex < w && therey >= 0 && therey < h)
                        {
                            if (visited[therey][therex] != 1 && f[therey][therex] == -1)
                            {
                                cout << dist + 1;
                                return 0;
                            }
                            if (visited[therey][therex] != 1 && f[therey][therex] == 0)
                            {
                                qx.push(therex);
                                qy.push(therey);
                            }
                        }
                    }
                    qx.pop();
                    qy.pop();
                    size--;
                    if (size == 0)
                    {
                        dist++;
                        size = qx.size();
                    }
                }
            }
        }
    }
}
```

* x값과 y값을 담기 위해 qx, qy라는 튜플 2개를 사용하였다.

---

# 마인크래프트 2

## 설명
이전 문제와 다르게, 각 칸끼리 이동할 때 드는 시간이 다르다. 각 칸을 정점으로 두고 인접한 칸끼리 가중치(거리)가 (캐는데 걸리는 시간 + 1)인 간선으로 연결하면, 그래프의 최단 경로 탐색 알고리즘을 적용하는 문제임을 알 수 있다. 따라서 다익스트라 알고리즘을 사용하면 ~~쉽게~~ 풀 수 있다.

## Dijkstra (다익스트라)

* [Dijkstra](https://velog.io/@717lumos/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BCDijkstra-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)

```py
```

---

---

# comments
python code by *Junee* and c++ code by *Raehwan*