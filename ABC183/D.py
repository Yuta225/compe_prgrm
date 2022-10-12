n,w = list(map(int,input().split()))

demand = [0] * 220000

for _ in range(n):
    s, t, p = map(int,input().split())
    demand[s] += p
    demand[t] -= p

for i in range(1,220000):
    demand[i] += demand[i-1]#累積和

if w >= max(demand):
    print("Yes")
else:
    print("No")


""" p = [tuple(map(int, input().split())) for i in range(n)]

alll = [0 for i in range(w)]

for i in range(len(p)):
    for j in range(p[i][0],p[i][1]):
        alll[j] += p[i][2]
if w >= max(alll):
    print("Yes")
else:
    print("No")


aaaa """