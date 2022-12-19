from collections import Counter
s = input()
t = input()
cou = len(t)
for i in range(len(s)):
    if s[i] != t[i]:
        cou = i +1
        break
print(cou)