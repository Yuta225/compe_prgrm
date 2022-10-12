N,W = map(str, input().split())
a = list(N)
b = list(W)
c = [int(s) for s in a]
d = [int(s) for s in b]
x = 0
y = 0

for i in range(len(c)):
    x+= c[i]
for i in range(len(d)):
    y += d[i]

if x >= y:
    print(x)
else:
    print(y)