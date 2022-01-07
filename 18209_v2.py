### 시간 초과 ###

import sys
input = sys.stdin.readline

# input
speech = input()
umm = ""
ummLength = 0

# process & output
i = 0
isUmm = True
endSpeech = False
temp = ""
tempLength = 0
while not endSpeech:
	currentChar = speech[i]

	if currentChar == 'u':
		temp += '1'
		tempLength += 1
	elif currentChar == 'm':
		temp += '0'
		tempLength += 1

	# a 'word' ended
	elif currentChar == ' ' or currentChar == '\n':
		if isUmm:
			umm += temp
			ummLength += tempLength
		isUmm = True
		temp = ""
		tempLength = 0
		# speech ended
		if currentChar == '\n':
			endSpeech = True

	# if a 'word' contains digits or letters other than lowercase u and m
	# it is not umm-coded word
	elif '0'<=currentChar<='9' or 'A'<=currentChar<='Z' or 'a'<=currentChar<='z':
		isUmm = False

	i += 1

# output
for i in range(0, ummLength, 7):
	print(chr(int("0b"+umm[i : i+7], 2)), end='')