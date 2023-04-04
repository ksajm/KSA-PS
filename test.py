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