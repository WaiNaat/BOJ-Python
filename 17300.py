# input
pLen = int(input())
pattern = list(map(int, input().split()))
# process
'''
사용한 숫자는 set에 따로 저장
이미 사용한 점을 건너서 가는 경우는 if문으로 따로 처리
'''
used = set([pattern[0]])
cur = next = None
isPossible = True
for i in range(pLen - 1):
	cur = pattern[i]
	next = pattern[i + 1]
	# 다음 점이 이미 사용한 점인지 판단.
	if next in used:
		isPossible = False
		break
	# 다음 점으로 이동할 수 있는지 판단.
	if cur == 1:
		if (next == 3 and 2 not in used) or \
			(next == 7 and 4 not in used) or \
			(next == 9 and 5 not in used):
			isPossible = False
	elif cur == 2:
		if next == 8 and 5 not in used:
			isPossible = False
	elif cur == 3:
		if (next == 1 and 2 not in used) or \
			(next == 7 and 5 not in used) or \
			(next == 9 and 6 not in used):
			isPossible = False
	elif cur == 4:
		if (next == 6 and 5 not in used):
			isPossible = False
	elif cur == 6:
		if (next == 4 and 5 not in used):
			isPossible = False
	elif cur == 7:
		if (next == 1 and 4 not in used) or \
			(next == 3 and 5 not in used) or \
			(next == 9 and 8 not in used):
			isPossible = False
	elif cur == 8:
		if next == 2 and 5 not in used:
			isPossible = False
	elif cur == 9:
		if (next == 1 and 5 not in used) or \
			(next == 3 and 6 not in used) or \
			(next == 7 and 8 not in used):
			isPossible = False
	if not isPossible: break		
	# 다음 점으로
	used.add(next)
# output
print("YES" if isPossible else "NO")