N,Q = map(int, input().split())
l = set()
ans = []
for i in range(Q):
    T,A,B = map(int, input().split())
    if T == 1:
        l.add((A,B))
    if T == 2:
        if (A,B) in l:
            l.remove((A,B))
    if T == 3:
        if (A,B) in l and (B,A) in l:
            ans.append("Yes")
        else:
            ans.append("No")

for i in range(len(ans)):
    print(ans[i])