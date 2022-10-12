N = str(input())
p = list(map(int,input().split()))
ans = 0
tall = p[0]
for i in range(1,len(p)):
    x = p[i] - tall
    if x < 0:
        ans += abs(x)
    if p[i] > tall:
        tall = p[i]

print(ans)