import math
N = int(input())
a = list(map(int,input().split()))
x =[]
for i in range(N-1):
    t = math.gcd(a[i], a[i+1])
    if t != 1:
        x.append(t)
if not x:
    o = math.gcd(a[0],a[-1])
    print(o)
else:
    y = []
    s = len(x)
    t = len(a)
    for j in range(s):
        count = 0
        for k in range(t):
            if a[k]%x[j] == 0:
                count += 1
        y.append(count)
    u = max(y)
    inde = y.index(u)
    print(x[inde])