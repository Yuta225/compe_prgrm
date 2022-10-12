N,K = map(int, input().split())
ans = N
for i in range(K):
    if ans % 200 == 0:
        ans = ans//200
    else:
        sans = str(ans)
        sans += "200"
        ans = int(sans)
print(ans)