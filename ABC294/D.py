N,Q = map(int, input().split())
call = []
reca = []
num = 1

for i in range(Q):
    val = list(map(int,input().split()))
    if val[0] == 1:
        call.append(num)
        num += 1
    elif val[0] == 2:
        for j in range(len(call)):
            if call[j] == val[1]:
                call.pop(j)
    else:
        x = call[0]
        call.pop(0)
        reca.append(x)

[print(i) for i in reca]