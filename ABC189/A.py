N = str(input())
a = N[:1]
a += a +a
if a == N:
    print("Won")
else:
    print("Lost")