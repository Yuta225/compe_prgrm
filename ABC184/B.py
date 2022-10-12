N,X = list(map(int,input().split()))
S = str(input())

for i in range(N):
    a = S[:1]
    g = len(S)-1
    S = S[-g::]
    if a == 'o':
        X += 1
    if a == 'x' and  X >0:
        X -= 1
print(X)