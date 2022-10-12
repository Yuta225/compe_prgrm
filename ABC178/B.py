a, b,c,d = map(int, input().split())
x = []
x.append(a*c)
x.append(a*d)
x.append(b*c)
x.append(b*d)
print(max(x))