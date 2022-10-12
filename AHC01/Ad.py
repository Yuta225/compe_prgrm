import copy

n = int(input())
ry = [[]for i in range(16)]
for i in range(n):
    x,y,r = map(int, input().split())
    if 0 <= x and x < 2500:
        t = 0
    elif 2500 <= x and x < 5000:
        t = 4
    elif 5000 <= x and x < 7500:
        t = 8
    elif 7500 <= x and x < 10000:
        t = 12
    
    if 0 <= y and y < 2500:
        t += 0
    elif 2500 <= y and y < 5000:
        t += 1
    elif 5000 <= y and y < 7500:
        t += 2
    elif 7500 <= y and y < 10000:
        t += 3
    
    ry[t].append(x)
    ry[t].append(y)

for i in range(16):
    san = copy.deepcopy(ry[i])
    

"""
p = [tuple(map(int, input().split())) for i in range(n)]
https://atcoder.jp/contests/ahc001/tasks/ahc001_a
"""