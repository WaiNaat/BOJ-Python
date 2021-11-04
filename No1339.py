import sys
input = sys.stdin.readline

# input & process
N = int(input())
letters = {}

for i in range(N):
	word = input().rstrip()
	wordLength = len(word)
	for i in range(wordLength):
		letter_value = 10 ** (wordLength - 1 - i)
		if word[i] in letters.keys():
			letters[word[i]] += letter_value
		else:
			letters[word[i]] = letter_value

val = sorted(letters.values(), reverse=True)
valLength = len(val)
sol = 0
for i in range(valLength):
	sol += val[i] * (9 - i)

# output
print(sol)