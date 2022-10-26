N,W = map(int, input().split())
l = [0 for i in range(W)]
for i in range(N):
    p = input()
    for j in range(len(p)):
        if p[j] == "#":
            l[j] += 1
L=[str(a) for a in l]
L=' '.join(L)
print(L)