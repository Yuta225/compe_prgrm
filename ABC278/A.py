N,W = map(int, input().split())
p = list(map(int,input().split()))
for i in range(W):
    p.pop(0)
    p.append(0)
print(*p)