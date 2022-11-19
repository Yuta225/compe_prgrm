N,W = map(str, input().split())

x = 0
while x == 0:
    if len(N) == 1:
        a = 0
        b = int(N[0])
    else:
        a = int(N[0])
        b = int(N[1])

    if len(W) == 1:
        c = 0
        d = int(W[0])
    else:
        c = int(W[0])
        d = int(W[1])
    
    if int(str(a)+str(c)) < 24 and int(str(b) + str(d)) < 60:
        x += 1
    
    W = str(int(W) + 1)
    if int(W) == 60:
        W = str(0)
        N = str(int(N) + 1)
    if int(N) == 24:
        N = str(0)

print(int(str(a)+str(b)),int(str(c) + str(d)))
