N = int(input())
a = []
b = []
count = 0
u = 0

while(N != count):
    count += 1
    x,y = map(int,input().split())
    a.append(x)
    b.append(y)

for i in range(N):
    t = (a[i]-1)*(a[i])//2
    s = b[i]*(b[i]+1)//2
    u += s-t

print(u)