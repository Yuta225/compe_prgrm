N = int(input())
S = [str(input()) for i in range(N)]
T = list(dict.fromkeys(S))
U = []
V = set()

for i in range (len(T)):
    a = T[i]
    b = a[0]
    if b == "!":
        V.add(a)
    else:
        U.append(a)

for i in range(len(U)):
    if "!" + U[i] in V:
        print(U[i])
        exit()
print("satisfiable")