N = int(input())
N,W = map(int, input().split())
p = list(map(int,input().split()))
p = [tuple(map(int, input().split())) for i in range(N)]

s = [input() for _ in range(9)]
