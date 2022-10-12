s = str(input())
t = str(input())

ans = len(t)
lengtht = len(t)

for i in range(0,len(s) - len(t)+1):
    count = 0
    hikaku = s[i:i+lengtht]
    for j in range(len(t)):
        if hikaku[j] != t[j]:
            count +=1
    if ans > count:
        ans = count
print(ans)