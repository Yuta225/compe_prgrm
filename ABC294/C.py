N,M = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

X = N + M
A_i = 0
B_i = 0
A_il = []
B_il = []

for i in range(X):
    if N == len(A_il):
        #Bしか見なくていい
        B_il.append(i+1)
    elif M == len(B_il):
        #Aしか見なくていい
        A_il.append(i+1)
    else:
        if A[A_i] < B[B_i]:
            A_il.append(i+1)
            A_i += 1
        else:
            B_il.append(i+1)
            B_i += 1


u=[str(a) for a in A_il]
i=[str(a) for a in B_il]

print(' '.join(u))
print(' '.join(i))