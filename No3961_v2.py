import sys
input = sys.stdin.readline

### functions ###
# getDistance(char ch1, char ch2) returns the distance btw ch1, ch2
def getDistance(ch1,ch2):
	x1, y1 = coord[ch1]
	x2, y2 = coord[ch2]
	return abs(x1-x2) + abs(y1-y2)


### main ###

# make "coordinate table" of alphabets
# EX. coord['q']=(0,0) , coord['m']=(2,6)
coord = {}
line0 = "qwertyuiop"
line1 = "asdfghjkl-"
line2 = "zxcvbnm---"
for i in range(10):
	coord[line0[i]] = (i, 0)
	coord[line1[i]] = (i, 1)
	coord[line2[i]] = (i, 2)

# input, process, output
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
	for word, distance in words:
		sys.stdout.write("%s %d\n" % (word, distance))