import collections

N = int(input())
a = list(map(int,input().split()))

c = collections.Counter(a)
count = 0
xx = 0

s,t = zip(*c.most_common())

xx =0
for i in range(len(c)):
    if t[i] > s[i]:
        xx = t[i] - s[i]
    elif s[i]>t[i]:
        xx = t[i]
    count += xx
    xx =0

print(count)