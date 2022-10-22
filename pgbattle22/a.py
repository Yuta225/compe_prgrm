N,Q = map(int, input().split())
l = [0 for i in range(N)]
for i in range(Q):
    x,y = map(int, input().split())
    for j in range(x-1,y):
        l[j] += 1
m = 0
for i in range(N):
    if l[i] % 2  != 0:
        m += 1
print(m)        