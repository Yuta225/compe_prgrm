import math

N = int(input())
N_min = math.ceil(math.sqrt(N))
N_max = math.floor(math.log2(N))
count = set()

for i in range(2,N_max+1):
    for j in range(2,N_min+1):
        if j**i <= N:
            count.add(j**i)
        else:
            break

print(N -len(count))

""" 
https://vermee81-coding-memo.hatenablog.jp/entry/2021/02/28/070000
"""