N,T = map(int, input().split())
A = list(map(int,input().split()))
allp = sum(A)
val = T - (T//allp)*allp

for i in range(len(A)):
    valc = val
    val -= A[i]
    if val < 0:
        print(i+1, valc)
        break