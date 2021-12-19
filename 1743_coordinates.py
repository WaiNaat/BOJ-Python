import sys
input = sys.stdin.readline

# functions
def DFS(x, y):
	move = ((1, 0), (-1, 0), (0, 1), (0, -1))

	stack = [(x, y)]
	cnt = 1
	hallway[y][x] = -1

	while stack:
		x, y = stack.pop()
		for dx, dy in move:
			x2 = x + dx
			y2 = y + dy
			if not 0 <= x2 < width or not 0 <= y2 < height: 
				continue
			if hallway[y2][x2] == 1:
				hallway[y2][x2] = -1
				cnt += 1
				stack.append((x2, y2))
	return cnt

# input
height, width, K = map(int, input().split())
hallway = [[0 for _ in range(width)] for _ in range(height)]
for _ in range(K):
	y, x = map(int, input().split())
	hallway[y - 1][x - 1] = 1

# process
max_size = 0
for y in range(height):
	for x in range(width):
		if hallway[y][x] == 1:
			size = DFS(x, y)
			if max_size < size: max_size = size

# output
print(max_size)