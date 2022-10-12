N = int(input())

name = []
high = []
for i in range(N):
    a,b = map(str, input().split())
    name.append(a)
    high.append(int(b))

indices = [*range(len(high))]
sorted_indices = sorted(indices, reverse= True,key=lambda j: high[j])
sorted_num = [name[j] for j in sorted_indices]

print(sorted_num[1])