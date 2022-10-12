x,y= map(int, input().split())
a = x
b =y
if x >y:
    a = y
    b =x
a = a +3
if a > b:
    print("Yes")
else:
    print("No")