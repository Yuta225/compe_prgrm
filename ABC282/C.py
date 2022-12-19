N = int(input())
S = list(input())
flag = 0
for i in range(N):
    if S[i] == '"':
        flag += 1
    if flag%2 == 0 and S[i] == ",":
        S[i] = "."
print("".join(S))
