import sys
input = sys.stdin.readline

# functions
# getCoord(char ch) returns the coordinate of input char ch
# ex. getCoord(q)=0,0 and getCoord(m)=6,2
def getCoord(ch):
	line0 = "qwertyuiop"
	line1 = "asdfghjkl-"
	line2 = "zxcvbnm---"
	for i in range(10):
		if ch == line0[i]: return i, 0
		elif ch == line1[i]: return i, 1
		elif ch == line2[i]: return i, 2

# getDistance(char ch1, char ch2) returns the distance btw ch1, ch2
def getDistance(ch1,ch2):
	x1, y1 = getCoord(ch1)
	x2, y2 = getCoord(ch2)
	return abs(x1-x2) + abs(y1-y2)


# main
t = int(input())

for i in range(t):
	userInput, wordNo = input().split() # get user input
	inputLen = len(userInput)
	wordNo = int(wordNo)
	words = {}

	for j in range(wordNo):
		# get word candidate and compute distance
		word = input().rstrip()
		distance = 0
		for k in range(inputLen):
			distance += getDistance(userInput[k], word[k])
		words[word] = distance
	
	# sort
	words = sorted(words.items(), key=lambda x: (x[1], x[0]))
	
	#output result
	for k in range(wordNo):
		sys.stdout.write(words[k][0]+" %d\n" % words[k][1])
