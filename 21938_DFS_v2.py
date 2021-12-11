import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# functions
def countObj(width, height, T):
	cnt = 0
	dx = (1, -1, 0, 0)
	dy = (0, 0, 1, -1)
	for row in range(height):
		for col in range(width):
			if img[row][col] >= T:
				cnt += 1
				DFS(row, col, width, height, T, dx, dy)
	return cnt

def DFS(row, col, width, height, T, dx, dy):
	img[row][col] = -1
	for i in range(4):
		row2 = row + dy[i]
		col2 = col + dx[i]
		if not 0 <= col2 < width or not 0 <= row2 < height:
			continue
		if img[row2][col2] >= T:
			DFS(row2, col2, width, height, T, dx, dy)

# input
height, width = map(int, input().split())
img = [[] for _ in range(height)]
for i in range(height):
	line = list(map(int, input().split()))
	for j in range(width):
		img[i].append(line[3 * j] + line[3 * j + 1] + line[3 * j + 2])
T = int(input()) * 3

# process & output
print(countObj(width, height, T))