N, A, B = map(int, input().split())
ab_list = []

for i in range(N+1):
    wo = i
    so = str(i)
    nu = 0
    for j in range(len(so)):
        nu += int(so[j])
    
    if A <= nu and nu <= B:
        ab_list.append(i)

print(sum(ab_list))