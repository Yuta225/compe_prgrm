N = int(input())

for i in range(1,1000001):
    y = str(i)
    yy = int(y+y)
    if yy > N:
        ans = i-1
        break
print(ans)