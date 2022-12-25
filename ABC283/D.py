S = input()
open_w = []
for i in range(len(S)):
    if S[i] == ")":
        open_w.clear()
    elif S[i] == "(":
        pass
    else:
        if S[i] in open_w :
            print("No")
            exit()
        else:
            open_w.append(S[i])
print("Yes")