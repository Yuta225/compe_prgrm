N = int(input())
p = list(map(int,input().split()))
cou = 10000000

for i in range(len(p)):
    a = p[i]
    cc = 0
    while a%2 == 0 and a > 1:
        a = a // 2
        cc += 1
    if cou > cc:
        cou = cc

print(cou)