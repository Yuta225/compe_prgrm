T = int(input())
cou = [0 for i in range(T)]
for i in range(T):
    num = int(input())
    p = list(map(int,input().split()))
    for j in range(num):
        if p[j] % 2 == 1:
            cou[i] += 1
for i in range(T):
    print(cou[i])