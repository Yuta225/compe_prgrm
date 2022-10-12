import itertools
n,k = list(map(int,input().split()))
p = [tuple(map(int, input().split())) for i in range(n)]
x =n-1
a =list(itertools.permutations(range(x)))

allcost = []
for i in range(len(a)):
    count = 0
    cost = 0
    for j in range(n):
        count += 1
        if count == 1:
            cost += p[0][a[i][j]+1]
            
        if count != 1 and count != n:
            cost += p[a[i][j-1]+1][a[i][j]+1]

        if count == n:
            cost += p[a[i][j-1]+1][0]
            allcost.append(cost)
            count = 0
            cost = 0
print(allcost.count(k))
