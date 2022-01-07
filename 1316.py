import sys
input = sys.stdin.readline

# input & process
N = int(input())
cnt = 0

for _ in range(N):
	letters = [0 for _ in range(26)]
	word = input().rstrip()

	last = -1
	isGroupWord = True

	for i in range(len(word)):
		ch = ord(word[i]) - 97
		# letter changed and it has appeared before
		if letters[ch] > 0 and last != ch:
			isGroupWord = False
			break;
		letters[ch] += 1
		last = ch
	if isGroupWord: cnt += 1

# output
print(cnt)