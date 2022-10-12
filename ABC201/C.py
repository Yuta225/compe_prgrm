#場合分けして散っていった
import math

N = list(input())
x = [i for i, x in enumerate(N) if x == 'o']
y = [i for i, x in enumerate(N) if x == '?']
a = len(x)
b = len(y)
ans = 0

if a == 4:
    ans = 1
elif a < 4:
    if 0 < a < 4 or 0 < b < 4:
        if a == 3 and b >= 1:
            ans = math.factorial(a+1)*b + 36
        elif a == 2:
            if b == 0:
                ans = 14
            elif b == 1:
                ans = (math.factorial(4)//math.factorial(2))*3 + 14
            elif b == 2:
                ans = (math.factorial(4)//2)*b + (math.factorial(4)//math.factorial(2))*3 + 14
            elif b > 2:
                ans = (math.factorial(4)//2)*b + math.factorial(b)//(2*math.factorial(b-2)) + 14
        elif a == 1:
            if b == 0:
                ans = 1
            elif b ==1:
                ans = 15
            else:
                #ans = 1 + 14*b + math.factorial(b)//(2*math.factorial(b-2))*
                ans = (math.factorial(4)//math.factorial(3)) + (math.factorial(4)//math.factorial(2)) + math.factorial(b)//(1*math.factorial(b-1)) + 1

print(ans)

