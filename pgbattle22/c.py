N = int(input())
p = list(map(int,input().split()))
in1 = [i for i, x in enumerate(p) if x == 1]
print(in1)
for i in range(len(in1)):
    remove_ind = in1[i]
    val = p[in1[i]]
    remove_cou = 0
    print("初期値",val)
    for j in range(p[in1[i]]+1,len(p)):
        if p[j] - val == 1:
            remove_cou += 1
            val = p[j]
        else:
            break
    in1 = [n-remove_ind for n in in1]
    print(in1[i],remove_cou)
    for k in range(remove_cou):
        p.pop(remove_ind)
    print(i,p,in1)

print(sum(p))