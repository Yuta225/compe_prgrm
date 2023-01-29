N = int(input())
p = []
for i in range(N):
    x = input()
    p.append(x)

for i in range(1,N+1):
    print(p[-i])