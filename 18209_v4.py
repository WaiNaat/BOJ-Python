import sys
input = sys.stdin.readline

# input
words = input().split()
umm = []
ummLength = 0

# process
for word in words:
	isUmm = True
	wordLength = len(word)
	temp = []
	tempLength = 0

	for i in range(wordLength):
		# finds 'u' or 'm'
		if word[i] == 'u':
			temp.append('1')
			tempLength += 1
		elif word[i] == 'm':
			temp.append('0')
			tempLength += 1
		# if a 'word' contains digits or letters other than lowercase u and m
		# it is not umm-coded word
		elif '0'<=word[i]<='9' or 'A'<=word[i]<='Z' or 'a'<=word[i]<='z':
			isUmm = False
			break
	
	if isUmm:
		umm += temp
		ummLength += tempLength

# output
for i in range(0, ummLength, 7):
	sys.stdout.write(chr(int(''.join(umm[i : i+7]), 2)))