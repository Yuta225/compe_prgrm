import math

A,B = map(int, input().split())
ans = 1

for i in range(B,0,-1):
    num = B//i - (A-1)//i
    if num >= 2:
        ans = i

print(ans)