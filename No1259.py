import sys
input = sys.stdin.readline

num = input().rstrip()

while num != '0':

	left = 0
	right = len(num)-1
	isPalin = True

	while left <= right:

		if num[left] != num[right]:
			isPalin = False
			break
		else:
			left += 1
			right -= 1

	if isPalin: print("yes")
	else: print("no")
	
	num = input().rstrip()