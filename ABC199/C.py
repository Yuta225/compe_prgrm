N = int(input())
S = str(input())
Q = int(input())
S = list(S)
ans = 0
for i in range(Q):
    t,a,b = map(int, input().split())
    if t == 1:
        S[a-1],S[b-1] = S[b-1],S[a-1]
    else:
        if ans == 0:
            ans = 1
        else:
            ans = 0

if ans == 0:
    k = S[:N]
    l = S[N:]
    S = l+k

print("".join(S))
