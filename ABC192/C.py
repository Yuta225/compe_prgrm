N,K = map(int, input().split())
ans = 0

for i in range(K):
    St_N = str(N)
    list(St_N)
    g1 = sorted(St_N, key = int)
    g2 = sorted(St_N, reverse= True, key = int)
    ig1 = int("".join(g1))
    ig2 = int("".join(g2))
    N = ig2 - ig1
print(N)