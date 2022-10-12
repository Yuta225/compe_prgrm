n ,p = map(int,input().split())
str_list = [input() for _ in range(n)]
count = 0
print(str_list)
for k in range(n):
    for l in range(p):
        if str_list[k][l] == ".":
            if k != n-1:
                if str_list[k+1][l] == ".":
                    count += 1
            if l != p-1:
                if str_list[k][l+1] == ".":
                    count += 1

print(count)