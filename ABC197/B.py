h,w,x,y= map(int, input().split())
x -= 1
y -= 1
tat = []
yok = []

for i in range(h):
    a = list(map(str, input()))
    if i != x:
        tat.append(a[y])
    else:
        tat.append(a[y])
        for j in range(len(a)):
            yok.append(a[j])

print("縦",tat)
print("横",yok)
count = 0

for i in range(y+1,len(yok)):
    if yok[i] == ".":
        count += 1
    elif yok[i] == "#":
        break

yok.reverse()
for i in range(len(yok)-y,len(yok)):
    if yok[i] == ".":
        count += 1
    elif yok[i] == "#":
        break
    
for i in range(x+1,len(tat)):
    if tat[i] == ".":
        count += 1
    elif tat[i] == "#":
        break

tat.reverse()
for i in range(len(tat)-x,len(tat)):
    if tat[i] == ".":
        count += 1
    elif tat[i] == "#":
        break

print(count+1)