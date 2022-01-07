# input
N = int(input())
S = []
for i in range(N):
	S.append(input())

# process & output
length_T = 0
left = 0
right = N-1
while length_T < N:
	if S[left] < S[right]:
		print(S[left], end='')
		left += 1

	elif S[left] > S[right]:
		print(S[right], end='')
		right -= 1

	else:
		temp_l = left
		temp_r = right
		while temp_l < temp_r:
			printed = False
			temp_l += 1
			temp_r -= 1
			if S[temp_l] < S[temp_r]:
				print(S[left], end='')
				left += 1
				printed = True
				break
			elif S[temp_l] > S[temp_r]:
				print(S[right], end='')
				right -= 1
				printed = True
				break
				
		if (not printed) or left == right:
			print(S[left], end='')
			left += 1

	length_T += 1
	if length_T % 80 == 0:
		print('\n', end='')