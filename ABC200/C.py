N = int(input())
p = list(map(int,input().split()))
a = []
b = [0 for i in range(200)]
ans = 0

for i in range(N):
    x = p[i]%200
    b[x] += 1

for i in range(200):
    ans += (b[i]*(b[i]-1))//2

print(ans)