import math

N = str(input())
x = N.find('.')
if x == -1:
    print(N)
else:
    print(N[:x])