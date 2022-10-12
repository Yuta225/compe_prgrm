import re

S = str(input())
T = ""

for i in range(len(S)):
    x = S
    S = re.sub("([a-z])\\1", "", S)
    if x == S:
        break

for i in range(len(S)):
    if S[i] != "R":
        T += S[i]
    else:
        T = T[::-1]

for i in range(len(T)):
    x = T
    T = re.sub("([a-z])\\1", "", T)
    if x == T:
        break
print(T)
