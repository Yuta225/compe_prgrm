import random

N,W = map(int, input().split())
a = []
b = []

la = max(N,W)
mi = min(N,W)

if N >= W:
    for i in range(1,la+1):
        a.append(i)

    x = la - mi

    for i in range(1,mi+1):
        if i < mi:
            b.append(-1*i)
        else:
            zan = sum(a)
            mai = sum(b)
            b.append(-1*(zan+mai))

else:
    for i in range(1,la+1):
        a.append(-1*i)

    x = la - mi

    for i in range(1,mi+1):
        if i < mi:
            b.append(i)
        else:
            zan = sum(a)
            mai = sum(b)
            print(zan)
            print(mai)
            b.append(-1*(mai+zan))

c = a + b
print(" ".join(map(str, c)))
print("Aの数",len(a))
print("Bの数",len(b))
print(sum(a))
print(sum(b))
print("和",sum(c))