N = int(input())

K = N+1
t = N-1

for i in range (K):
    x = (i*(i+1))/2
    if x>K:
        count = i
        break

a = (count*(count+1))//2
b = (t*(t+1))//2
num = count+b-a

print(num)