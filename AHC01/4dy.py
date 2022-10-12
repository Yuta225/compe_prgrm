import copy

n = int(input())
ry = [[]for i in range(4)]
yonly = [[]for i in range(4)]
for i in range(n):
    x,y,r = map(int, input().split())
    if 0 <= x and x < 5000:
        t = 0
    elif 5000 <= x and x < 10000:
        t = 2
    if 0 <= y and y < 5000:
        t += 0
    elif 5000 <= y and y <10000:
        t += 1
    
    ry[t].append(x)
    ry[t].append(y)
    ry[t].append(i)
    ry[t].append(r//5000)
    yonly[t].append(y)
    yonly[t].append(i)
    yonly[t].append(r//5000)

def has_duplicates(seq):
    return len(seq) == len(set(seq))
output = [[] for i in range(n)]
for i in range(4):
    san = copy.deepcopy(yonly[i][0::3])
    sanr = copy.deepcopy(yonly[i][2::3])
    xan = copy.deepcopy(ry[i][0::4])
    xanr = copy.deepcopy(ry[i][3::7])
    if has_duplicates(san) == True:#横に切る
            indices = [*range(len(san))]
            sorted_indices = sorted(indices, key=lambda j: san[j])
            sorted_num = [san[j] for j in sorted_indices]
            zahyou = []
            length = len(san)
            
            count = 0
            if i == 0 or i == 2:
                last = 5000
                mae  = 0
            elif i == 1 or i == 3:
                last = 10000
                mae  = 5000

            for k in range(length):
                if count != length-1:
                    zahyou.append(mae)
                    slash = sanr[sorted_indices[k]] - sorted_num[k] +mae 
                    if slash <= 0:
                        uuu = sorted_num[k]+1
                    elif slash+sorted_num[k] < sorted_num[k+1]:
                        uuu = sorted_num[k] + slash
                    elif slash+sorted_num[k] >= sorted_num[k+1]:
                        uuu = sorted_num[k+1]
                    zahyou.append(uuu)
                    mae = uuu
                elif count == length-1:
                    zahyou.append(mae)
                    zahyou.append(last)
                count+=1
            count = 0
            for l in range(0,length*2,2):
                if 0 <= i and i < 2:
                    a = 0
                    c = 5000
                elif 2 <= i and i < 4:
                    a = 5000
                    c = 10000
                b = zahyou[l]
                d = zahyou[l+1]
                output[yonly[i][sorted_indices[count]*3+1]] = str(a) + " " + str(b) + " " + str(c) + " " + str(d)
                count += 1
    elif has_duplicates(xan) == True:
        indices = [*range(len(xan))]
        sorted_indices = sorted(indices, key=lambda j: xan[j])
        sorted_num = [xan[j] for j in sorted_indices]
        zahyou = []
        length = len(xan)

        count = 0
        if 0 <= i and i < 2:
            last = 5000
            mae  = 0
        elif 2 <= i and i < 4:
            last = 10000
            mae  = 5000
        
        for k in range(length):
            if count != length-1:
                zahyou.append(mae)
                slash = sanr[sorted_indices[k]] - sorted_num[k] +mae 
                if slash <= 0:
                    uuu = sorted_num[k]+1
                elif slash+sorted_num[k] < sorted_num[k+1]:
                    uuu = sorted_num[k] + slash
                elif slash+sorted_num[k] >= sorted_num[k+1]:
                    uuu = sorted_num[k+1]
                zahyou.append(uuu)
                mae = uuu
            elif count == length-1:
                zahyou.append(mae)
                zahyou.append(last)
            count+=1
        count = 0
        for l in range(0,length*2,2):
            if i == 0 or i == 2:
                b = 0
                d = 5000
            elif i == 1 or i == 3:
                b = 5000
                d = 10000
            a = zahyou[l]
            c = zahyou[l+1]
            output[ry[i][sorted_indices[count]*4+2]] = str(a) + " " + str(b) + " " + str(c) + " " + str(d)
            count += 1
    
    else:#x座標を参照して縦に切るプログラムを書いて提出
        for j in range(len(san)):
            a = ry[i][j*4]
            b = ry[i][j*4+1]
            c = a+1
            d = b+1
            output[ry[i][j*4+2]] = str(a) + " " + str(b) + " " + str(c) + " " + str(d)

for i in range(n):
    print(output[i])