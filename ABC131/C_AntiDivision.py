import math
A, B, C, D = map(int, input().split())

fx = B - A + 1
y = C*D//math.gcd(C,D)
t = B//C - (A-1)//C + B//D - (A-1)//D - (B//y - (A-1)//y)

print(fx -t)