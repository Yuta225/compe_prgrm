N,M = map(int, input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))

x =[]
x.extend(A-B)
x.extend(B-A)
x = sorted(x)
x = ' '.join(map(str, x))
print(x)