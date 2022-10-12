def comb(n, k):#重複組み合わせ
    ret = 1
    #print(n+1,k+1,n-k+1)
    for i in range(1, n + 1):
        ret *= i
    for i in range(1, k + 1):#仕切り
        ret //= i
    for i in range(1, n - k + 1):#〇
        ret //= i
    return ret

L = int(input())
X = L - 12
ans = comb(X + 11, 11)
print(ans)