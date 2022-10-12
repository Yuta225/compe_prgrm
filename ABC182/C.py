n = input()
n = list(n)
judge = false

if sum(list)%3 == 0:
    ans = 0

print(ans)

""" 
for bits in product((True, False), repeat=l):
    digit_sum = 0  # 消してない桁の和です
    score = 0  # 桁を消した数で、少ないほうがうれしいです
    for i, bit in enumerate(bits):
        if bit:
            # 上からi桁目を消さずに使います
            digit_sum += A[i]
        else:
            # 上からi桁目を消します
            score += 1

    if digit_sum % 3 == 0:
        #  3の倍数になる消し方なら、最小値を更新します
        ans = min(ans, score)

if ans == l:
    # 3の倍数にならなかったので、-1を出力します
    print(-1)
else:
    print(ans)
 """


""" import copy
N = str(input())
x = (list(N))
x.reverse()
x = [int(s) for s in x]
a =len(x)
count = 0
u = copy.copy(x)
for i in range(a):
    sum3 = sum(u)
    if sum3%3 == 0:
        print(len(x)-len(u))
        exit(0)
    else:
        u = copy.copy(x)
        del u[i]
        print(u)
        count += 1
    if count = a:
        for k in range(a): """