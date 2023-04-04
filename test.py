r1, r2, r3 = input().split()
r1 = int(r1)
r2 = int(r2)
r3 = int(r3)

rooms = {
    r1: '김준이',
    r2: '김창하',
    r3: '김래환'
}
del rooms[ min(r1, r2, r3) ]
del rooms[ max(r1, r2, r3) ]

for ans in rooms:
    print(ans)