import math
N = int(input())
x = 0

for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            x += math.gcd(i,j,k)
print(x)