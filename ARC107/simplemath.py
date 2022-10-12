A, B, C = map(int,input().split())

print(A*(A+1)//2*B*(B+1)//2*C*(C+1)//2%998244353)

"""
学び：1からnまでの和の出し方

1 + 2 + 3 + .... + n = n*(n+1)//2
"""

"""
TLEのお方

x = 0
for i in range(1,A+1):
    for j in range(1,B+1):
        for k in range(1, C+1):
            x = x + i*j*k
print(x%998244353) """