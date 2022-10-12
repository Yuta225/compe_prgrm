N = int(input())
p = list(map(int,input().split()))
ans = 0
x = []
for i in range(N):
    x.append(p[i]%100)
b = list(set(x))
c = []

for i in b:
    count = 0
    for j in range(len(x)):
        if i == x[j]:
            count+= 1
        if count >= 2:
            c.append(i)
            break

if len(c) == 0:
    print(0)
    exit()
else:
    d = [[]for i in range(len(c))]
    for i in range(N):
        for j in range(len(c)):
            if x[i] == c[j]:
                d[j].append(p[i])
                break
    
    for i in range(len(d)):
        for j in range(len(d[i])):
            for k in range(j+1,len(d[i])):
                if (d[i][j]-d[i][k])%200 == 0:
                    ans += 1

print(ans)