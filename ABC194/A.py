x,y = map(int, input().split())
a = x + y
if a >= 15 and y >= 8:
    print(1)
elif a >= 10 and y >= 3:
    print(2)
elif a >= 3:
    print(3)
else:
    print(4)