N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

x = max(a)
y = min(b)
ans = y-x+1
if ans < 0:
    print(0)
else:
    print(ans)
