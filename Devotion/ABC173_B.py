N = int(input())
S = [str(input()) for i in range(N)]

A = S.count("AC")
B = S.count("WA")
C = S.count("TLE")
D = S.count("RE")
print("AC x",A)
print("WA x",B)
print("TLE x",C)
print("RE x", D)