N = int(input())
S = str(input())
Q = int(input())
S = list(S)
flag = False

for i in range(Q):
    t,a,b = map(int, input().split())
    if t == 1:
        if flag == False:
            S[a-1],S[b-1] = S[b-1],S[a-1]
        else:
            if a >N:
                x = a-N-1
            else:
                x = N + a - 1
            if b >N:
                y = b-N-1
            else:
                y = N + b - 1
            S[x],S[y] = S[y],S[x]
    else:
        flag = not bool(flag)

if flag == True:
    k = S[:N]
    l = S[N:]
    S = l+k

print("".join(S))