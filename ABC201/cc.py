
N = input()
ans = 0

for i in range(10000):
    flag = [False]*10
    now  = i
    kk = True
    for j in range(4):
        flag[now%10] = True
        now = now //10
    for j in range(10):
        if N[j] == "o" and flag[j] != True:
            kk = False
        if N[j] == "x" and flag[j] == True:
            kk = False
    ans += kk
print(ans)