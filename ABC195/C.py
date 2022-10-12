N = int(input())
x = str(N)
ln = len(x)

if 4 <= ln and  ln <= 6:
    x = N -999
    ans = x*1
elif 7 <= ln and  ln <= 9:
    x = N - 999999
    ans = x*2 +999000 
elif 10 <= ln and  ln <= 12:
    x = N - 999999999
    ans = x*3 + 999000000*2 + 999000  
elif 13 <= ln and  ln <= 15:
    x = N - 999999999999
    ans = x*4 + 999000000000*3 + 999000000*2 + 999000  
elif ln == 16:
    x = N - 999999999999999
    ans = x*5 + 999000000000000*4+ 999000000000*3 + 999000000*2 + 999000  
else:
    ans = 0

print(ans)
