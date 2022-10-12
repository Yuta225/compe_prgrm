H,A = map(int, input().split())

x =H//A
y = H%A

if y != 0:
    x+= 1
print(x)