""" 配列の大小を比べるとき（今回であればsとtの各要素でどっちが辞書的に後ろか）各要素ごとやらんでも配列ぽんと渡して待っても"""
""" if文でどこまで出来るかを知っといた方がいい """
s = list(input())
t = list(input())

ss = sorted(s)
tt = sorted(t, reverse=True)

""" c = len(ss)
d = len(tt)

if d > c:
    x = d-c
    for i in range(x):
        ss.append("")
count = 0
dd = math.ceil(d/2) """

if tt > ss:
    print("Yes")
else:
    print("No")


""" for i in range(d):
    if ss[i] < tt[i]:
        count += 1
    if count >= dd:
        print("Yes")
        exit()

print("No") """


