n = int(input())
p = [tuple(map(int, input().split())) for i in range(n)]
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            x1, y1 = p[i]
            x2, y2 = p[j]
            x3, y3 = p[k]
            y = ((y2-y1)/(x2-x1))*(x3-x1)+y1
            if y3 == y:
                print("Yes")
                exit()
print("No")