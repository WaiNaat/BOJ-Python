import sys
input = sys.stdin.readline
from itertools import product, permutations
from collections import deque
# class
class Floor:
	def __init__(self, floor):
		'''
		direction 0/1/2/3은 각각 정위치부터 시계방향으로 돌렸을 때의 방향
		'''
		self.direction = 0
		self.floor = floor
	
	def getGrid(self, row, col):
		# 정위치
		if self.direction == 0:
			return self.floor[row][col]
		# 시계 90도 회전
		elif self.direction == 1:
			return self.floor[col][4 - row]
		# 시계 180도 회전
		elif self.direction == 2:
			return self.floor[4 - row][4 - col]
		# 시계 270도 회전
		else:
			return self.floor[4 - col][row]

# function
def bfs(current_min_score):
	'''
	bfs를 돌리는 데 속도를 빠르게 하기 위해
	1. 시작점이 사람이 갈 수 없는 공간이면 즉시 실패 처리
	2. 현재 최저 이동 횟수(current_min_score)보다 이동횟수가 많아지면 즉시 실패 처리
	'''
	# 시작점이 0이면 실패
	if maze[0].getGrid(0, 0) == 0:
		return current_min_score

	visited = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]
	visited[0][0][0] = 1
	q = deque([(0, 0, 0, 0)])

	while q:
		x, y, z, cnt = q.popleft()
		# 현재 이동횟수가 전체 최저 이동 횟수보다 많으면 무조건 실패
		if cnt > current_min_score:
			break
		# 도착점 도착시 성공
		if x == y == z == 4:
			return cnt
		# 6방향 탐색
		for dx, dy, dz in maze_moves:
			x2 = x + dx
			y2 = y + dy
			z2 = z + dz
			if not 0 <= x2 < 5 or not 0 <= y2 < 5 or not 0 <= z2 < 5:
				continue
			if visited[z2][y2][x2] == 0 and maze[z2].getGrid(y2, x2) == 1:
				visited[z2][y2][x2] = 1
				q.append((x2, y2, z2, cnt + 1))

	return current_min_score

# input
maze_original = []
for _ in range(5):
	floor = [tuple(map(int, input().split())) for _ in range(5)]
	maze_original.append(Floor(floor))
# process
'''
어떤 미로에 대해 bfs로 탈출 여부와 이동 횟수를 알 수 있음.
각 판은 회전이 되니까 4^5=1024가지 미로 제작 가능.
각 판을 쌓는 방법도 5! = 120가지.
이 1024*120개 미로에 대해 bfs를 돌리면 될 듯?

미로를 빠르게 '돌리는' 방법
미로의 각 층을 class로 만들어서 현재 어느 방향인지 저장하는 변수를 추가로 둔다.
'''
sol = 1234
maze_moves = ((1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1))
for maze in permutations(maze_original):
	maze = list(maze)
	for direction in product(range(4), repeat = 5):
		for i in range(5):
			maze[i].direction = direction[i]
		sol = bfs(sol)
	# 12가 이론상 최저 이동 횟수이므로 그 값 나왔으면 더 이상 계산 안 함
	if sol == 12:
		break
# output
print(sol if sol != 1234 else -1)