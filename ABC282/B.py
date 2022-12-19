N,M = map(int, input().split())
S = []
for i in range(N):
    ans = list(input())
    S.append(ans)
cou = 0
for i in range(N):
    for j in range(i+1,N):
        c = 0
        for k in range(M):
            if S[i][k] == "o" or S[j][k] == "o":
                c += 1
            else:
                break
            if c == M:
                cou += 1
print(cou)
        
