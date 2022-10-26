N = int(input())
p = list(map(int,input().split()))
p.insert(0,0)
l = [0 for i in range(2*N+1)]
l.insert(0,0)
for i in range(1,N+1):
    l[i*2] += l[p[i]] + 1
    l[i*2+1] += l[p[i]] + 1
for i in range(1,2*N+2):
    print(l[i])