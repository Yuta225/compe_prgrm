
N = int(input())
A = list(map(int,input().split()))

k = 0
sumA = 0
sumB = 0

for i in range(N):
    sumA += A[i]**2
sumB = sum(A)**2
print(N*sumA - sumB)