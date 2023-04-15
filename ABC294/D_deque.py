from collections import deque

N,Q = map(int, input().split())

#1 : 受付に呼ばれていない人のうち、最も小さい番号の人が受付に呼ばれる。
#2 x : 人 x が初めて受付に行く。(ここで、人 x はすでに 1 回以上受付に呼ばれている。)
#3 : すでに受付に呼ばれているが受付に行っていない人のうち、最も小さい番号の人が再度呼ばれる。

call = []

for i in range(Q):
    val = list(map(int,input().split()))
    val = deque(val)
    print(val)
    #初：1
    if val[0] == 1:
        call.append(i + 1)
    #受付に行く：2
    elif val[0] == 2:
        call.deque(0)
    #3
    print(call)