import numpy
import math

N,X,Y = map(int, input().split())

u = math.sqrt(X**2+Y**2)
ans = u / N

if ans.is_integer() == False:
    if ans >= 1:
        ans += 1
    else:
        ans += 2
print(math.floor(ans))