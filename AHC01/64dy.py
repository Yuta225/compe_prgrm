import copy

n = int(input())
ry = [[]for i in range(25)]
yonly = [[]for i in range(25)]
for i in range(n):
    x,y,r = map(int, input().split())
    if 0 <= x and x < 2000:
        t = 0
    elif 2000 <= x and x < 4000:
        t = 5
    elif 4000 <= x and x < 6000:
        t = 10
    elif 6000 <= x and x <= 8000:
        t = 15
    elif 8000 <= x and x < 10000:
        t = 20
    
    if 0 <= y and y < 2000:
        t += 0
    elif 2000 <= y and y < 4000:
        t += 1
    elif 4000 <= y and y < 6000:
        t += 2
    elif 6000 <= y and y <= 8000:
        t += 3
    elif 8000 <= y and y < 10000:
        t += 4

    
    ry[t].append(x)
    ry[t].append(y)
    ry[t].append(i)
    ry[t].append(r//2000)
    yonly[t].append(y)
    yonly[t].append(i)
    yonly[t].append(r//2000)

def has_duplicates(seq):
    return len(seq) == len(set(seq))
output = [[] for i in range(n)]
for i in range(25):
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
            if i == 0 or i == 5 or i == 10 or i== 15 or i == 20:
                last = 2000
                mae  = 0
            elif i == 1 or i == 6 or i == 11 or i== 16 or i == 21:
                last = 4000
                mae  = 2000
            elif i == 2 or i == 7 or i == 12 or i== 17 or i == 22:
                last = 6000
                mae = 4000
            elif i == 3 or i == 8 or i == 13 or i== 18 or i == 23:
                last = 8000
                mae  = 6000
            elif i == 4 or i == 9 or i == 14 or i== 19 or i == 24:
                last = 10000
                mae  = 8000

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
                if 0 <= i and i < 5:
                    c = 2000
                    a = 0
                elif 5 <= i and i < 10:
                    a = 2000
                    c = 4000
                elif 10 <= i and i < 15:
                    a = 4000
                    c = 6000
                elif 15 <= i and i < 20:
                    a = 6000
                    c = 8000
                elif 20 <= i and i < 25:
                    a = 8000
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
        if 0 <= i and i < 5:
            mae = 0
            last = 2000
        elif 5 <= i and i < 10:
            mae = 2000
            last = 4000
        elif 10 <= i and i < 15:
            mae = 4000
            last = 6000
        elif 15 <= i and i < 20:
            mae = 6000
            last = 8000
        elif 20 <= i and i < 25:
            mae = 8000
            last = 10000
        
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
            if i == 0 or i == 5 or i == 10 or i== 15 or i == 20:
                d = 2000
                b  = 0
            elif i == 1 or i == 6 or i == 11 or i== 16 or i == 21:
                d = 4000
                b  = 2000
            elif i == 2 or i == 7 or i == 12 or i== 17 or i == 22:
                d = 6000
                b = 4000
            elif i == 3 or i == 8 or i == 13 or i== 18 or i == 23:
                d = 8000
                b  = 6000
            elif i == 4 or i == 9 or i == 14 or i== 19 or i == 24:
                d = 10000
                b  = 8000
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