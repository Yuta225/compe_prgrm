import math
S, P = map(int, input().split())
d = S**2 - 4*P
s1 = -1*(-S+math.sqrt(d))/2
s2 = -1* (-S-math.sqrt(d))/2

if s1+s2== S and s1*s2==P:
    print("Yes")
else:
    print("No")