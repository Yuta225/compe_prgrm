a,b,x,y = list(map(int,input().split()))

if a == b:
    print(x)

elif a>b:
    """ 降りるとき """
    if x >= y:
        cost = abs(a-b-1)*y+x
        print(cost)
    elif y > x:
        xx = x*2
        if y > xx:
            cost = abs(a-b-1)*2*x+x
            print(cost)
        else:
            cost = abs(a-b-1)*y + x
            print(cost)
elif b>a:
    """ 上る時 """
    if x >= y:
        cost = (b-a)*y+x
        print(cost)
    elif y > x:
        xx = x*2
        if y > xx:
            cost = (b-a)*2*x+x
            print(cost)
        else:
            cost = x+ abs(b-a)*y
            print(cost)
