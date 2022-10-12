"通ったやつ　stackで愚直にやる"
N = int(input())
s = str(input())
t =""
for i in range (N):
    x = s[:1]
    g = len(s)-1
    s = s[-g::]
    t += x
    if len(t) > 2 and t[-3::] == "fox":
        t = t[:-3]
print(len(t))    

""" 
最後の問題をTLEするお方
count = 1
t =[]
t.append(s)
i = 0
while count != 0:
    i += 1
    q =len(t[i-1])//3
    t.append(t[i-1].replace('fox', '', q))
    if 'fox' not in t[i]:
        print(len(t[i]))
        exit() 
"""