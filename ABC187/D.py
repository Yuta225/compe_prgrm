N = int(input())
X = 0
x = []
for i in range(N):
    A,B = map(int, input().split())
    X -= A
    x.append(2*A+B)
list.sort(x, reverse=True)
count = 0
for i in range(len(x)):
    X += x[i]
    count += 1
    if X > 0:
        break
print(count)