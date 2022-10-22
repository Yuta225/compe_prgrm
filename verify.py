import itertools
import math

N = int(input())
a = []
for i in range(N):
    x,y = map(int, input().split())
    a.append([x,y])
b = list(itertools.permutations(a))
val = []
for i in range(len(b)):
    x = 0
    for j in range(1,N):
        x += math.sqrt((b[i-1][j-1][0] - b[i-1][j][0])**2 + (b[i-1][j-1][1] - b[i-1][j][1])**2)
    val.append(x)
print(sum(val)/len(b))