s = input()
n = len(s)
stack = [0 for i in range(1000000)]
top = -1

for i in range(n): 
	top += 1
	stack[top] = s[i]
	if top>=3 and stack[top-3] + stack[top-2] + stack[top-1] + stack[top] == "PPAP":
		top -= 3

if top == 0 and stack[top] == "P":
	print("PPAP")
else:
	print("NP")