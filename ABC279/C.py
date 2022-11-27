H,W = map(int, input().split())
S_l = [[0 for i in range(H)] for i in range(W)]
T_l = [[0 for i in range(H)] for i in range(W)]
for i in range(H):
    x = input()
    for j in range(W):
        if x[j] == "#":
            S_l[j][i] += 1
for i in range(H):
    x = input()
    for j in range(W):
        if x[j] == "#":
            T_l[j][i] += 1
ss = sorted(S_l)
tt = sorted(T_l)
for i in range(W):
    if ss[i] != tt[i]:
        print("No")
        exit()
print("Yes")

