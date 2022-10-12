A = []
for i in range(3):
    x = list(map(int, input().split()))
    A.append(x)

M = [[False, False, False], [False, False, False], [False, False, False]]

N = int(input())

for i in range(N):
    b = int(input())
    for j in range(3):
        if b in A[j]:
            u = A[j].index(b)
            M[j][u] = True

Ans = "No"

for i in range(3):
    if M[i][0] and M[i][1] and M[i][2]:
        Ans = "Yes"
    
for i in range(3):
    if M[0][i] and M[1][i] and M[2][i]:
        Ans = "Yes"

if M[0][0] and M[1][1] and M[2][2]:
    Ans = "Yes"

if M[0][2] and M[1][1] and M[2][0]:
    Ans = "Yes"

print(Ans)