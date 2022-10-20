N = input()
N = N.replace("eraser", "")
N = N.replace("erase", "")
N = N.replace("dreamer", "")
N = N.replace("dream", "")
if N == "":
    print("YES")
else:
    print("NO")