S = str(input())
ans = "Yes"
for i in range(len(S)):
    if (i+1) %2 == 0 and S[i].islower() is True:
        ans = "No"
        break
    elif (i+1) %2 != 0 and S[i].isupper() is True:
        ans = "No"
        break

print(ans)