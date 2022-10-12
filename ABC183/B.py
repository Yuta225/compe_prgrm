x1,y1,x2,y2 = list(map(int,input().split()))
y2 =y2*-1
y =0
x =((x2-x1)/(y2-y1))*(y-y1)+x1
print('{:.10f}'.format(x))