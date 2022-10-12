h,w = map(int, input().split())
ten = []
h = []
b = []
maea = 0
maeb = 0
for i in range(h):
    N = str(input())
    if i>0:
        a = N.find("#")
        b = N.rfind("#")
        if maea != a:
            h.append(a,i)
        if maeb != b:
            b.append(b,i)
        maea = a
        maeb = b