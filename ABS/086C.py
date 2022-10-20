N = int(input())
sch = [[0,0,0]]
for i in range(N):
    t,x,y = map(int, input().split())
    sch.append([t,x,y])
for i in range(1,len(sch)):
    d = abs(sch[i-1][1] + sch[i-1][2] - sch[i][1] - sch[i][2])
    t = sch[i][0] - sch[i-1][0]
    a = d - t
    if a > 0:
        print("No")
        exit()
    if a < 0:
        if a % 2 != 0:
            print("No")
            exit()
print("Yes")