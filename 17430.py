import sys
input = sys.stdin.readline
# input
t = int(input())
for _ in range(t):
	n = int(input())
	lights = {}
	for _ in range(n):
		x, y = map(int, input().split())
		if x not in lights: lights[x] = set([])
		lights[x].add(y)
# process
	'''
	모든 가로등이 균형잡혀 있다면
	가로등이 있는 모든 x축들은
	모두 가로등이 있는 y축이 같아야 함.
	'''
	aux = None
	isBalanced = True
	for y in lights.values():
		if aux is None: aux = y
		elif aux != y:
			isBalanced = False
			break
# output
	print("BALANCED" if isBalanced else "NOT BALANCED")