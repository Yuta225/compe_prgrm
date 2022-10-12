N = int(input())
count = 0
x = "No"
for i in range(N):
    a, b = map(int, input().split())
    if a == b:
        count += 1
        if count == 3:
            x = "Yes"
    elif a != b and count > 0:
        count = 0

print(x)