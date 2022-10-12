N = int(input())
S = input()

r_c = S.count("R")
g_c = S.count("G")
b_c = S.count("B")

com = r_c * g_c * b_c
#print(com)
for i in range(N):
    for a in range(N):
        j = i + a
        k = j + a
        #print(i,j,k)
        if k >= N:
            break
        if S[i] == S[j] and S[i] != S[k] and S[j] != S[k]:
            com -= 1
print(com)

