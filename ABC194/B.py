N = int(input())
al = []
bl = []
for i in range(N):
    c = 0
    a, b = map(int, input().split())
    al.append(a)
    bl.append(b)

flag = 0
ma = min(al)
ma_inde = al.index(ma)
mb = min(bl)
mb_inde = bl.index(mb)

if ma_inde == mb_inde:
    nal = sorted(al)
    nbl = sorted(bl)
    tma = nal[1]
    tmb = nbl[1]
    if tma >= tmb:
        x = tmb
        c =0
    else:
        x = tma
        c = 1
    u = ma + mb
    if x < u:
        if c == 0:
            mb = x
        else:
            ma = x
    else:
        flag = 1

if flag == 0:
    if ma >= mb:
        print(ma)
    else:
        print(mb)
else:
    print(ma+mb)