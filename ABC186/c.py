N = int(input())
count = 0

for i in range(1, N+1):
    if ('7' not in str(i)) and ('7' not in oct(i)):
        count += 1
print(count)


""" N = int(input())
oct(N)[2:]

x1 = 0
x2 = 0
x3 = 0
x4 = 0
count = 0
for i in range (N):
    x1 = i/10
    x2 = i/100
    x3 = i/1000
    x4= i/10000
    if i % 7 == 0 or i % 10 == 7 or x1 % 10 == 7 or x2 % 10 == 7 or x3 % 10 == 7 or x4 %10 ==7:
        count += 1

print(count) """