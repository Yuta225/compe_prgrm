p = list(map(int,input().split()))
for i in range(len(p)):
    if p[i] == 1:
        p[i] = 6
    elif p[i] == 2:
        p[i] = 5
    elif p[i] == 3:
        p[i] = 4
    elif p[i] == 4:
        p[i] = 3
    elif p[i] == 5:
        p[i] = 2
    else:
        p[i] = 1

print(sum(p))