# input
word = input()
# process
'''
처음에 o가 나올때까지 w의 개수를 세면 됨.
'''
isValid = True
i = 0
while i < len(word):
	# w
	wCnt = 0
	while i < len(word) and word[i] == 'w':
		i += 1
		wCnt += 1
	if wCnt == 0: isValid = False
	# o
	cnt = 0
	while i < len(word) and word[i] == 'o':
		i += 1
		cnt += 1
	if cnt != wCnt: isValid = False
	# l
	cnt = 0
	while i < len(word) and word[i] == 'l':
		i += 1
		cnt += 1
	if cnt != wCnt: isValid = False
	# f
	cnt = 0
	while i < len(word) and word[i] == 'f':
		i += 1
		cnt += 1
	if cnt != wCnt: isValid = False
	if not isValid: break
# output
print(1 if isValid else 0)