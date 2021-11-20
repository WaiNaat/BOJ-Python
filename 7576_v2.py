import sys
from collections import deque
input = sys.stdin.readline

# function
def BFS(M, N):
	directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
	visited = [[0 for _ in range(M)] for _ in range(N)]
	maxDay = 0
	ripeCnt = 0

	while q:
		x, y = q.popleft()
		d = visited[y][x]
		ripeCnt += 1
		for dx, dy in directions:
			x2 = x + dx
			y2 = y + dy
			if not 0 <= x2 < M or not 0 <= y2 < N: continue
			if box[y2][x2] == 0 and visited[y2][x2] == 0:
				visited[y2][x2] = d + 1
				maxDay = max(maxDay, d+1)
				q.append((x2, y2))
	return maxDay, ripeCnt

# input
M, N = tuple(map(int, input().split()))
box = []
q = deque([])
tmtCnt = 0
for y in range(N):
	line = tuple(map(int, input().split()))
	for x in range(M):
		if line[x] == 1: 
			q.append((x, y))
			tmtCnt += 1
		elif line[x] == 0:
			tmtCnt += 1
	box.append(line)

# process
sol, ripeCnt = BFS(M, N)
if tmtCnt != ripeCnt: sol = -1

# output
print(sol)