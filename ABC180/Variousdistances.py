import math

N = int(input())
l = map(int,input().split())

l2 = []
l3 = []

for i in l:
    print(i)
    l2.append(abs(i))
    l3.append(abs(i)**2)

a = sum(l2)
c = max(l3)
b = (sum(l3))**0.5

print(a)
print(b)
print(c)