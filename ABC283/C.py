N = input()
x = "00"
num0 = N.count(x)
if num0 > 0:
    print(len(N)-num0)
else:
    print(len(N))