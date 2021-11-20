### 시간 초과 ###

import sys
from collections import deque
input = sys.stdin.readline

# function
def tomato(M, N):
	visited = [[1000000 for _ in range(M)] for _ in range(N)]
	for x in range(M):
		for y in range(N):
			# find ripe tomato at first day
			if box[y][x] == 1:
				BFS(x, y, M, N, visited)
	
	sol = 0
	for x in range(M):
		for y in range(N):
			# find unripe tomato
			if box[y][x] == 0 and visited[y][x] == 1000000:
				return -1
			# find max day
			elif 0 <= box[y][x] <= 1:
				sol = max(sol, visited[y][x])
	return sol

def BFS(x, y, M, N, visited):
	directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
	q = deque([])
	dMax = 0

	visited[y][x] = 0
	q.append((x, y))

	while len(q) != 0:
		x, y = q.popleft()
		d = visited[y][x]
		dMax = max(dMax, d)
		for dx, dy in directions:
			x2 = x + dx
			y2 = y + dy
			if not 0 <= x2 < M or not 0 <= y2 < N: continue
			# if adjacent tomato ripes earlier than before
			if box[y2][x2] == 0 and visited[y2][x2] > d+1:
				visited[y2][x2] = d + 1
				q.append((x2, y2))
	return dMax


# input
M, N = tuple(map(int, input().split()))
box = []
for _ in range(N):
	box.append( tuple(map(int, input().split())) )

# process & output
print(tomato(M, N))