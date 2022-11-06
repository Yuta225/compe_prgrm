def prevPermutation(str):

	n = len(str) - 1

	# Find largest index i such that
	# str[i - 1] > str[i]
	i = n
	while (i > 0 and str[i - 1] <= str[i]):
		i -= 1

	# if string is sorted in ascending order
	# we're at the last permutation
	if (i <= 0):
		return False, str

	# Note - str[i..n] is sorted in
	# ascending order

	# Find rightmost element's index
	# that is less than str[i - 1]
	j = i - 1
	while (j + 1 <= n and
		str[j + 1] < str[i - 1]):
		j += 1

	# Swap character at i-1 with j
	str = list(str)
	temp = str[i - 1]
	str[i - 1] = str[j]
	str[j] = temp
	str = ''.join(str)

	# Reverse the substring [i..n]
	str[i::-1]

	return True, str


N = int(input())
p = list(map(int,input().split()))
x = ""
for i in range(N):
    x += str(p[i])
print(x)

b, str = prevPermutation(x)
if (b == True):
    print("Previous permutation is", str)
else:
    print("Previous permutation doesn't exist")