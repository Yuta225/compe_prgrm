#bit全探索
def practice():
    money = 300
    item = (("みかん", 100), ("りんご", 200), ("ぶどう", 300))
    n = len(item)
    for i in range(2 ** n): #選ぶ(1)，選ばない(0)の2択がn個におこるので2^n
        bag = []
        total_m = 0
        for j in range(n):#組み合わせごとでずらしていく
            if ((i >> j) & 1): 
                bag.append(item[j][0])  # フラグが立っていたら bag に果物を詰める
                total_m += item[j][1]
        if total_m <= 300:
            print(total_m,bag)

def train_079C():
    n = input()
    item = (int(n[0]), int(n[1]), int(n[2]), int(n[3]))
    for i in range(2**3):
        total = 7
        l = []
        num = item[0]
        for j in range(3):
            if((i >> j) & 1):
                num += item[j+1]
                l.append("+")
            else:
                num -= item[j+1]
                l.append("-")
        if num == total:
            print(n[0],l[0],n[1],l[1],n[2],l[2],"=7",sep="")
            exit()



if __name__ == "__main__": 
    train_079C() 