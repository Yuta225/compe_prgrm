import itertools
N,K,D = map(int, input().split())
p = list(map(int,input().split()))
a = list(itertools.combinations(p, K))
maxv = 0
for i in range(len(a)):
    va = sum(a[-i])
    if va % D == 0:
        maxv = va
        break
if maxv > 0:
    print(maxv)
else:
    print(-1)