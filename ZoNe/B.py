N,D,H = map(int, input().split())
x2 = D
y2 = H
mx1 = 0
my1 = 0
ans = 0
for i in range(N):
    di,hi = map(int, input().split())
    x1 = di
    y1 = hi
    if ((y2-y1)/(x2-x1))*(-x1) + y1 > 0 and mx1 == 0 and my1 == 0:
        ans = ((y2-y1)/(x2-x1))*(-x1) + y1
        my1 = y1
        mx1 = x1
    elif mx1 != 0 and my1 != 0:
        if ((y2-my1)/(x2-mx1))*(x1-mx1) + my1 < y1 and ((y2-y1)/(x2-x1))*(-x1) + y1 > 0:
            ans = ((y2-y1)/(x2-x1))*(-x1) + y1
            my1 = y1
            mx1 = x1

if ans < 0:
    ans = 0

print(ans)

"""             print('こえてない')
            print(((y2-my1)/(x2-mx1))*(x1-mx1))
            print(y1)
            ans = ((y2-y1)/(x2-x1))*(-x1) + y1
            print("ans",ans) """