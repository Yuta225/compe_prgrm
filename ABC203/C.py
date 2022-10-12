import numpy as np

N,W = map(int, input().split())
x = []
x[0] = W
for i in range(N):
    a,b = map(int, input().split())
    if x[a] == -1:
        x[a] = b-1
    else:
        x[a] += b
print(x)
y = np.cumsum(x)
y = list(y)
print(y)
print(y.index(0))