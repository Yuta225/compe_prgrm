N = str(input())
he = str(N[0])
mi = str(N[1:-1])
si = str(N[-1])
if he.isalpha() == True and si.isalpha() == True and mi.isdigit() and int(mi)>=100000 and int(mi)<=999999 and len(mi) == 6:
        print("Yes")
else:
    print("No")