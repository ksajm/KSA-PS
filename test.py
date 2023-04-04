r1, r2, r3 = map(int, input().split())

rooms = {
    '김준이': r1,
    '김창하': r2,
    '김래환': r3
}

rooms = sorted(rooms.items(), key = lambda x:x[1])
print(rooms[1][0])