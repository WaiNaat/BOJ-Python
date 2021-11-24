# input
s = input()
bomb = input()
stack = []
# process
for i in range(len(s)):
	stack.append(s[i])
	if len(stack) >= len(bomb) and ''.join(stack[ len(stack) - len(bomb) : ]) == bomb:
		for _ in range(len(bomb)): stack.pop()
# output
print(''.join(stack)) if stack else print("FRULA")