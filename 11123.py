import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def countGroup(H, W):
	cnt = 0
	for row in range(H):
		for col in range(W):
			if pasture[row][col] == '#':
				cnt += 1
				DFS(row, col)
	return cnt

def DFS(y, x):
	pasture[y][x] = '.'

	dx = [1, -1,  0, 0]
	dy = [0,  0, -1, 1]
	for i in range(4):
		x2 = x + dx[i]
		y2 = y + dy[i]
		if not 0 <= x2 < W or not 0 <= y2 < H: continue
		if pasture[y2][x2] == '#':
			DFS(y2, x2)


# input
T = int(input())
for _ in range(T):
	H, W = map(int, input().split())
	pasture = [list(input().rstrip()) for _ in range(H)]
# process & output
	print(countGroup(H, W))