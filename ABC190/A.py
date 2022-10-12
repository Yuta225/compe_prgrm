A,B,C = map(int, input().split())
if C == 1:
    B = B -1
if A > B:
    print("Takahashi")
elif A == B:
    print("Aoki")