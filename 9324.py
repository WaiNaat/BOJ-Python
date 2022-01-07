import sys
input = sys.stdin.readline
output = sys.stdout.write

# functions
# monkey()
# gets a message and determines whether it is valid or not.
def monkey():
	count = [0 for i in range(26)] # count[0]: occurence of 'A', ... , [25]: 'Z'
	message = input()
	currentChar = message[0]
	i = 0
	
	while currentChar != '\n':
		# count occurence of current letter
		current = ord(currentChar) - 65
		count[current] += 1
		i += 1

		# if current letter was its 3rd appearence
		# peek next character and determine the correctness of the message
		if count[current] == 3:
			nextChar = message[i]
			if currentChar != nextChar:
				return False
			else: # if it was not fake, should skip the 'noised' char
				i += 1
				count[current] = 0
		
		currentChar = message[i]

	return True

# main
n = int(input())
for i in range(n):
	if monkey(): output("OK\n")
	else: output("FAKE\n")