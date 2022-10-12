N = str(input())

aAns = N.count("a")
bAns = N.count("b")
cAns = N.count("c")

ans = max(aAns, bAns, cAns)
if ans == aAns:
    print("a")
elif ans == bAns:
    print("b")
else:
    print("c")