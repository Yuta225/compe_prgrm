import itertools

N = int(input())
p = list(map(int,input().split()))
a = sorted(p)
x = list(itertools.permutations(a))
#print(x)
for i in range(len(x)):
    cou = 0
    for j in range(N):
        if x[i][j] == p[j]:
            cou += 1
        if cou == N:
            print(*x[i-1])