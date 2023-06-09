from queue import PriorityQueue

w, h = map(int, input().split())
location = []
timeCost = [[float('inf') for i in range(w)] for i in range(h)]
direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
queue = PriorityQueue()
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
    time, x, y = arg
    
    if location[y][x] == -1 and timeCost[y][x] != 0:
        hasAnswer = True
        print(timeCost[y][x])
        return

    for move in direction:
        nextX = x + move[0]
        nextY = y + move[1]
        if not isInRange(nextX, nextY):
            continue
        nextTime = time + location[nextY][nextX] + 1
        if location[nextY][nextX] == -1: nextTime += 1

        # nextTime is the minimum time to reach location[nextY][nextX] is in this situation (알고리즘에 의해 증명 가능)
        if nextTime < timeCost[nextY][nextX]:
            timeCost[nextY][nextX] = nextTime
            queue.put((nextTime, nextX, nextY))

def startDijkstra():
    for y in range(h):
        for x in range(w):
            if location[y][x] == -1:
                timeCost[y][x] = 0
                checkNextBlock((0, x, y))
                return

getInput()
startDijkstra()

while not hasAnswer:
    checkNextBlock(queue.get())