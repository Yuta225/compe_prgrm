N = int(input())
han = (2**N)//2
A = list(map(int,input().split()))
x = A[:han]
y = A[han:]

tx = max(x)
tx_ind = x.index(tx) + 1
ty = max(y)
ty_ind = y.index(ty) + 1

if tx > ty:
    print(han+ty_ind)
else:
    print(tx_ind)