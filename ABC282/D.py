from collections import deque
import copy

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)


cou = 0
for i in range(N):
    for j in range(i+1,N):
        ans = "YES"
        GG = copy.copy(G)
        GG[i-1].append(j-1)
        GG[j-1].append(i-1)
        color = [-1 for _ in range(N)] 
        for v in range(N):
            if color[v] != -1: 
                continue
            deq = deque([])
            color[v] = 0
            deq.append(v)
            while len(deq) > 0:
                qv = deq.popleft()
                for nv in GG[qv]:
                    if color[nv] != -1:
                        if color[nv] == color[qv]:
                            ans = "NO"
                        continue
                    
                    color[nv] = 1 - color[qv]
                    deq.append(nv)
        if ans =="YES":
            cou += 1

print(cou)