H,W = map(int, input().split())
s = 0
for i in range(H):
    a = input()
    t = a.count("#")
    s += t
print(s)