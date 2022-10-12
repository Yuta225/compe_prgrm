n,x = map(int, input().split())
A = list(map(int,input().split()))
B = ""
for i in range(len(A)):
    if A[i] != x:
        B = B + str(A[i])
        B = B + " "
print(B[:-1])