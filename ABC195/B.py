A, B, W = list(map(int, input().split()))
W*= 1000

ans = []

for i in range(1, 10**6+1):
    if A <= W/i <= B:
        ans.append(i)

if ans:
    print(min(ans),max(ans))
else:
    print('UNSATISFIABLE')