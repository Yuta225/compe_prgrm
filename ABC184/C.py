r1,c1 = list(map(int,input().split()))
r2,c2 = list(map(int,input().split()))
a = r2 - r1
b = c2 - c1
c = r2 + r1
d = c2 + c1

if r1-r2 == 0 and c1-c2 == 0:
    ans = 0
elif a == b or a == -b:
    ans = 1
elif abs(a)+abs(b)<=3:
    ans = 1
elif abs(a)+abs(b)<=6:
    ans = 2
elif c%2 == d%2:
    ans = 2
elif abs(a+b) <= 3 or abs(a - b) <= 3:
    ans = 2
else:
    ans = 3
print(ans)