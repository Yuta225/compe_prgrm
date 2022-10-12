N,M,T = map(int, input().split())
p = [tuple(map(int, input().split())) for i in range(M)]
x = len(p)
mmax = N
c = 0
for i in range(x):
    if c == 0:
        N = N - (p[i][0])
    else:
        N = N - (p[i][0]-p[i-1][1])
    if N <=0:
        print("No")
        exit()
    N = N + (p[i][1] - p[i][0])
    c+=1
    if N>mmax:
        N = mmax
    tt = p[i][1]

N =N -(T-tt)
if N>0:
    print("Yes")
else:
    print("No")