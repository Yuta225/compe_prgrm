import math
n=int(input())
x=1
lcm=1
for i in range(1,n+1):
  lcm=(lcm*i)//math.gcd(lcm,i)
print(lcm+1)


""" 
import numpy as np
from collections import Counter
import re
N = int(input())

arr = [0 for i in range(30)]

def factorization(n):
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            if arr[i-1]< cnt:
                arr[i-1] = cnt
    if temp!=1 and arr[temp-1] == 0:
        arr[temp-1] = 1
    return arr

for i in range(N-1):
    factorization(i+2)

z = np.nonzero(arr)
text = "".join(map(str, z))
e = re.sub("\\D","",text)
d = list(e)
d = [int(s) for s in d]
c = []

for i in range(len(d)):
    c.append(arr[d[i]])

x = 1
for i in range (len(d)):
    x =x* (d[i]+1)**c[i]

print(x+1) """