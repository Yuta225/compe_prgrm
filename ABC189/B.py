N,X = map(int, input().split())
alsum = 0
for i in range(N):
    a, b = map(int, input().split())
    alsum += a*b
    if alsum > X*100:
        print(i+1)
        exit()
print(-1)