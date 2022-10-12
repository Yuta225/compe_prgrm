N = int(input())
p = list(map(int,input().split()))
ans = 0
aa = 0
bb = max(p)
mae = 0

for i in range(1,bb+1):
    for j in range(N):
        if p[j] > i:
            aa += 1
    ans += (bb-i)*aa -mae
    mae = i
    aa = 0
print(ans%(10**9+7))