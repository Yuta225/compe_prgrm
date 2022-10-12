p = list(map(int,input().split()))
dup = [x for x in set(p) if 3 > p.count(x) > 1]
if dup != []:
    pp = [n for n in p if n!=dup[0]]
    ans = pp[0]
else:
    ans = 0
print(ans)
