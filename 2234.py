import sys
input = sys.stdin.readline

# function
def dfs(row, col, room_cnt):
	'''
	스택을 사용한 dfs.
	'''
	visited[row][col] = room_cnt
	cnt = 1
	stack = [(row, col)]

	while stack:
		r, c = stack.pop()

		for r2, c2 in castle[r][c]:
			if visited[r2][c2] == 0:
				visited[r2][c2] = room_cnt
				cnt += 1
				stack.append((r2, c2))
	
	return cnt

# input
col, row = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(row)]

# process
'''
일단 주어진 입력을 해석해서 그래프 형태로 만들 수 있으면
dfs/bfs로 쉽게 1번과 2번 문제 해결 가능.

그럼 3번은 어떻게??
각 방을 탐색할 때 방별로 '번호'를 붙여 줌.
(visited에 해당 통로가 몇 번 방 소속인지 저장)

방 개수와 크기 측정 이후에
각 통로를 확인해서 본인과 맞닿아 있는 다른 방 번호를 확인 가능.
'''
# castle 배열에 본인이 가진 벽이 아니라 본인에서 이동 가능한 통로 좌표 저장
# 각 통로의 네 방향을 확인해 이동 가능한 방향을 저장.
for r in range(row):
	for c in range(col):
		wall = castle[r][c]
		castle[r][c] = []
		# 서쪽
		if wall & 0b0001 == 0:
			castle[r][c].append((r, c - 1))
		# 북쪽
		if wall & 0b0010 == 0:
			castle[r][c].append((r - 1, c))
		# 동쪽
		if wall & 0b0100 == 0:
			castle[r][c].append((r, c + 1))
		# 남쪽
		if wall & 0b1000 == 0:
			castle[r][c].append((r + 1, c))

# 방 개수 및 크기 측정
room_size = [0]
room_cnt = 0
visited = [[0 for _ in range(col)] for _ in range(row)]

for r in range(row):
	for c in range(col):
		if visited[r][c] == 0:
			room_cnt += 1
			room_size.append(dfs(r, c, room_cnt))

# 각 방과 인접한 다른 방의 번호를 찾아 계산.
max_room_size_sum = 0
directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

for r in range(row):
	for c in range(col):
		cur_room = visited[r][c]

		for dr, dc in directions:
			r2 = r + dr
			c2 = c + dc
			
			if not 0 <= r2 < row or not 0 <= c2 < col: continue
			adj_room = visited[r2][c2]

			if cur_room != adj_room and \
				max_room_size_sum < room_size[cur_room] + room_size[adj_room]:
				max_room_size_sum = room_size[cur_room] + room_size[adj_room]

# output
print(room_cnt)
print(max(room_size))
print(max_room_size_sum)