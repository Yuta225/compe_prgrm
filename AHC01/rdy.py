import copy

n = int(input())
ry = [[]for i in range(16)]
yonly = [[]for i in range(16)]
for i in range(n):
    x,y,r = map(int, input().split())
    if 0 <= x and x < 2500:
        t = 0
    elif 2500 <= x and x < 5000:
        t = 4
    elif 5000 <= x and x < 7500:
        t = 8
    elif 7500 <= x and x < 10000:
        t = 12
    
    if 0 <= y and y < 2500:
        t += 0
    elif 2500 <= y and y < 5000:
        t += 1
    elif 5000 <= y and y < 7500:
        t += 2
    elif 7500 <= y and y < 10000:
        t += 3
    
    ry[t].append(x)
    ry[t].append(y)
    ry[t].append(i)
    ry[t].append(r//2500)
    yonly[t].append(y)
    yonly[t].append(i)
    yonly[t].append(r//2500)

def has_duplicates(seq):
    return len(seq) == len(set(seq))
output = [[] for i in range(n)]
for i in range(16):
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
            if i == 0 or i == 4 or i == 8 or i== 12:
                last = 2500
                mae  = 0
            elif i == 1 or i == 5 or i == 9 or i== 13:
                last = 5000
                mae  = 2500
            elif i == 2 or i == 6 or i == 10 or i== 14:
                last = 7500
                mae = 5000
            elif i == 3 or i == 7 or i == 11 or i== 15:
                last = 10000
                mae  = 7500

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
                if 0 <= i and i < 4:
                    a = 0
                    c = 2500
                elif 4 <= i and i < 8:
                    a = 2500
                    c = 5000
                elif 8 <= i and i < 12:
                    a = 5000
                    c = 7500
                elif 12 <= i and i < 16:
                    a = 7500
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
        if 0 <= i and i < 4:
            last = 2500
            mae  = 0
        elif 4 <= i and i < 8:
            last = 5000
            mae  = 2500
        elif 8 <= i and i < 12:
            last = 7500
            mae = 5000
        elif 12 <= i and i < 16:
            last = 10000
            mae  = 7500
        
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
            if i == 0 or i == 4 or i == 8 or i== 12:
                b = 0
                d = 2500
            elif i == 1 or i == 5 or i == 9 or i== 13:
                b = 2500
                d = 5000
            elif i == 2 or i == 6 or i == 10 or i== 14:
                b = 5000
                d = 7500
            elif i == 3 or i == 7 or i == 11 or i== 15:
                b = 7500
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