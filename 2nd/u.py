import math

N,W = map(int, input().split())
ans = 1
hani = math.floor(N/2)

for i in range(W,W-N-1,-1):
    ans = i
    