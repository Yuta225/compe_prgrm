import itertools

N = int(input())
p = [tuple(map(int, input().split())) for i in range(N)]
count = 0
for x in itertools.combinations(p, 2):
    a = (x[1][1]- x[0][1])/(x[1][0]-x[0][0])
    if -1 <= a and a <=1:
        count += 1
print(count)