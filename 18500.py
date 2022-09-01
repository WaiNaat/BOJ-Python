'''
bfs/dfs를 이용하면 클러스터가 떠 있는지 아닌지 알 수 있음
	떠 있다면 해당 클러스터엔 맨 바닥열 미네랄이 없음

클러스터 낙하 구현?
	bfs돌릴때 클러스터의 구성요소들 좌표 기억
	해당 좌표들을 한칸씩 떨어뜨림
	단 하나라도 다른 클러스터 또는 바닥과 만나면 정지
'''
import sys
from collections import deque
input = sys.stdin.readline

# constant
directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

# functions
def break_mineral(cave, C, height, isLeft):
	if isLeft:
		for c in range(C):
			if cave[height][c] != '.':
				cave[height][c] = '.'
				return
	else:
		for c in range(C-1, -1, -1):
			if cave[height][c] != '.':
				cave[height][c] = '.'
				return

def find_floating_cluster(cave, R, C):
	visited = [[False for _ in range(C)] for _ in range(R)]

	for r in range(R):
		for c in range(C):

			if cave[r][c] == '.' or visited[r][c]:
				continue

			q = deque([(r, c)])
			cluster_coords = set()
			is_floating = True

			while q:
				r, c = q.popleft()

				if visited[r][c]: continue
				visited[r][c] = True
				cluster_coords.add((r, c))
				
				if r == R - 1:
					is_floating = False

				for dr, dc in directions:
					r2 = r + dr
					c2 = c + dc

					if not 0 <= r2 < R or not 0 <= c2 < C or visited[r2][c2] or cave[r2][c2] == '.':
						continue

					q.append([r2, c2])
			
			if is_floating:
				return cluster_coords
				
	return None

def gravity(cave, R, C, coords):
	for r, c in coords:
		cave[r][c] = '.'

	while True:
		temp = set()
		for r, c in coords:
			if r + 1 == R or cave[r + 1][c] != '.':
				draw_cluster(cave, coords)
				return
			else:
				temp.add((r + 1, c))

		coords = temp

def draw_cluster(cave, coords):
	for r, c in coords:
		cave[r][c] = 'x'

# input
R, C = map(int, input().split())
cave = [list(input().rstrip()) for _ in range(R)]
N = int(input())
stick_height = map(lambda x: R - int(x), input().split())

# process
left_flag = False

for stick in stick_height:
	# 부수기
	left_flag = not left_flag
	break_mineral(cave, C, stick, left_flag)

	# 떠 있는 클러스터 찾기
	floating_cluster = find_floating_cluster(cave, R, C)

	if floating_cluster is None:
		continue

	# 클러스터 낙하
	gravity(cave, R, C, floating_cluster)

# output
sol = [''.join(cave[r]) for r in range(R)]
print('\n'.join(sol))