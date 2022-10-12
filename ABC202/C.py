import collections

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

ca = collections.Counter(A)
cc = collections.Counter(C)
ans = 0
print(ca)
print(B)
print(cc)
for k,v in ca.items():
    for l,w in cc.items():
        if k == B[l-1]:
            ans += v*w
print(ans)


""" for i in range(len(X)):
    a = ca[X[i]]
    b = cb[X[i]]
    c = cc[X[i]]
    Y.append(a*b*c)

if Y == []:
    print(0)
else:
    print(sum(Y)) """


""" C = list(C)
print(C)
ans = 0

for i in range(0,N):
    for j in range(0,len(C)):
        print(i,j)
        print(C[j])
        x =C[j]-1
        if A[i] == B[x]:
            ans += 1
print(ans) 

for i in range(len(X)):
    t = []
    t.append(A.count(X[i]))
    t.append(B.count(X[i]))
    t.append(C.count(X[i]))
    t.sort()
    Y.append(t[1])
"""
