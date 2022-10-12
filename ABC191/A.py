v,t,s,d = map(int, input().split())

st = v*t
en = v*s
if st <= d and d<=en:
    print("No")
else:
    print("Yes")