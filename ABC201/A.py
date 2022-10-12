a,b,c = map(int, input().split())

if a-b == b-c or b-a == a-c or a-c == c-b:
    print("Yes")
else:
    print("No")