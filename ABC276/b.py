N,M = map(int, input().split())
cou = [[] for i in range(N)]

for i in range(M):
    A,B = map(int, input().split())
    cou[A-1].append(B)
    cou[B-1].append(A)

for i in range(N):
    cou[i] = sorted(cou[i])

for i in range(N):
    if len(cou[i]) == 0:
        print(0)
    else:
        print(len(cou[i]), *cou[i])