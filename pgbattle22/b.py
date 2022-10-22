N = int(input())
num = list(map(int,input().split()))
indices = [*range(len(num))]
sorted_indices = sorted(indices, reverse=True,key=lambda i: -num[i])
l = []
for i in range(N,2*N):
    l.append(sorted_indices[i])
l.sort()
for i in range(len(l)):
    print(l[i]+1)