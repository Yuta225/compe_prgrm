N = str(input())

def judge(string): 
    return string.find(string[::-1])
ln = list(N)
if len(ln) != ln.count("0"):
    while N[-1] == "0":
        N = N[:-1]
        if N[0] == "0":
            N = N[1:]
    a = judge(N)
else:
    a = 0

if a == 0:
    print("Yes")
else:
    print("No")