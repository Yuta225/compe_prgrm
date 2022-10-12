import math
N = int(input())
a = list(map(int,input().split()))
y = math.gcd(a[0], a[len(a)-1])

for i in range(N-1):
    if y > math.gcd(a[i], a[i+1]):
        y = math.gcd(a[i], a[i+1])
print(y)