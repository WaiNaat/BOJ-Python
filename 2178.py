import sys
from collections import deque
input = sys.stdin.readline

# function
def BFS(N, M):
	# visited[y][x] stores vertex (x,y)'s depth in spanning tree
	visited = [[0 for _ in range(M)] for _ in range(N)]
	q = deque([])

	visited[0][0] = 1
	q.append((0, 0))

	while len(q) != 0:
		x, y = q.popleft()
		d = visited[y][x]
		if x == M-1 and y == N-1: return d
		# down
		if y+1 < N and maze[y+1][x] == '1' and visited[y+1][x] == 0:
			visited[y+1][x] = d+1
			q.append((x, y+1))
		# right
		if x+1 < M and maze[y][x+1] == '1' and visited[y][x+1] == 0:
			visited[y][x+1] = d+1
			q.append((x+1, y))
		# up
		if y > 0 and maze[y-1][x] == '1' and visited[y-1][x] == 0:
			visited[y-1][x] = d+1
			q.append((x, y-1))
		# left
		if x > 0 and maze[y][x-1] == '1' and visited[y][x-1] == 0:
			visited[y][x-1] = d+1
			q.append((x-1, y))
	return -1


# input
N, M = tuple(map(int, input().split()))
maze = []
for _ in range(N):
	maze.append(input().rstrip())

# process & output
print(BFS(N, M))