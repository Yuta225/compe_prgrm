N = str(input())
n = []
for i in range(len(N)):
    n.append(int(N[i]))
m = []
for i in range(len(n)):
    if n[i] == 6:
        m.append("9")
    elif n[i] == 9:
        m.append("6")
    else:
        x = str(n[i])
        m.append(x)
m.reverse()
print("".join(m))