t = int(input())

for i in range(t):
    N = int(input())
    divisors = set()
    for j in range(1, int(N**0.5)+1):
        if N % j == 0:
            divisors.add(j)
            if j != N // j:
                divisors.add(N//j)

    ki = 0
    gu = 0
    for s in divisors:
        if s %2 == 0:
            gu += 1
        else:
            ki += 1
    if ki > gu:
        print("Odd")
    elif gu > ki:
        print("Even")
    else:
        print("Same")
