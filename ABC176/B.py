N = str(input())
list(N)
Ni= [int(n) for n in N]
ans = 0
for i in range(len(Ni)):
    ans += Ni[i]

if ans%9 == 0:
    print("Yes")
else:
    print("No")