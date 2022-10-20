N,W = map(int, input().split())
for i in range(N+1):
    for j in range(N+1):
        if i + j <= N:
            s = W - (10000 * i + 5000 * j)
            if s // 1000 ==  (W - (10000 * i + 5000 * j))/1000 and  i+j+ s//1000 == N:
                print(i, j, s//1000)
                exit()
print("-1 -1 -1")