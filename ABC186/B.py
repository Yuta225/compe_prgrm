import itertools

N,W = map(int, input().split())

grid = []
for i in range(N):
    array = list(map(int, input().strip().split()))
    grid.append(array)

t = list(itertools.chain.from_iterable(grid))

minva = min(t)
summ =0

for i in range(len(t)):
    summ += t[i] - minva

print(summ)
