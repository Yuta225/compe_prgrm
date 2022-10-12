import math

N = int(input())
p = list(map(int,input().split()))
a = 0
b = 0
for i in range(N):
    a += abs(p[i])
    b += p[i]**2
    p[i] = abs(p[i])

b = math.sqrt(b)
c = max(p)

print(a)
print('{:.15f}'.format(b))
print(c)