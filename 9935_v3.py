# input
s = list(input())
bomb = list(input())
b = len(bomb)
last = bomb[-1]
stack = []
# process
for ch in s:
	stack.append(ch)
	if ch == last and stack[-b : ] == bomb:
		del stack[-b: ]
# output
print(''.join(stack)) if stack else print("FRULA")