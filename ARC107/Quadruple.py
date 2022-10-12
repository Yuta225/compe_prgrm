N, K= map(int,input().split())

count = 0

#a+b-c-d =K
#x =a + b, y =c + d

for x in range(1, 2*N+1):
    y = x - K
    if y > 2 or 2*N < y:
        continue
    x_c = (x-max(x-N,1) - (x-min(x-1,N)))+1
    y_c = (y-max(y-N,1) - (y-min(y-1,N)))+1
    ans += x_c * y_c

print(ans)



""" 
TLEのお方

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            for l in range(1, N+1):
                x  = i + j - k - l 
                if (x ==K):
                    count = count +1
print(count)"""