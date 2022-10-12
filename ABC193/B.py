N = int(input())
res = 0
for i in range(N):
    a,p,x = map(int, input().split())
    if x - a > 0:
        if res == 0:
            res = p
        elif p < res:
            res = p

if res != 0:
    print(res)
else:
    print(-1)
