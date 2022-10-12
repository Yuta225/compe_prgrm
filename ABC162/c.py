from math import gcd
N = int(input())
x = 0

for i in range(1,N+1):
    for j in range(1,N+1):
        a = gcd(i,j)
        for k in range(1,N+1):
            x+= gcd(a,k)
print(x)