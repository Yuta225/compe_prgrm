N,M = map(int, input().split())
ex_N = []
for i in range(M):
    flg = 0
    x, y = map(int, input().split())
    if len(ex_N) != 0:
        for j in range(len(ex_N)):
            if x in ex_N[j] or y  in ex_N[j]:
                eac = ex_N[j]
                eac.append(x)
                eac.append(y)
                eac_s = set(eac)
                ex_N[j] = list(eac_s)
                flg += 1
                break
    if flg == 0:
        ex_N.append([x,y])

if M == 0:
    print(N)
else:
    print(len(ex_N))