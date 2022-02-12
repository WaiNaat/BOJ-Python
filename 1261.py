import sys, heapq
input = sys.stdin.readline
# constant
INF = 12345
# input
col, row = map(int, input().split())
maze = [input().rstrip() for _ in range(row)]
# process
'''
다음 이동 장소가 벽일 경우 비용은 1, 아니면 비용 0.
다익스트라 알고리즘 사용.
'''
h = [(INF, r, c) for r in range(row) for c in range(col)]
h[0] = (0, 0, 0)
heapq.heapify(h)

smash = [[INF for _ in range(col)] for _ in range(row)]
smash[0][0] = 0

visited = [[0 for _ in range(col)] for _ in range(row)]

dir = ((1, 0), (-1, 0), (0, 1), (0, -1))
while h:
	smash_cnt, r, c = heapq.heappop(h)
	if visited[r][c] == 1: continue
	visited[r][c] = 1
	# 상하좌우를 확인하고 벽 부수는 횟수 반영.
	for dx, dy in dir:
		r2 = r + dy
		c2 = c + dx
		if not 0 <= r2 < row or not 0 <= c2 < col: continue
		if visited[r2][c2] == 1: continue
		# 다음 위치가 벽이면 비용을 1로 설정.
		cost = 0 if maze[r2][c2] == '0' else 1
		if smash_cnt + cost < smash[r2][c2]:
			smash[r2][c2] = smash_cnt + cost
			heapq.heappush(h, (smash_cnt + cost, r2, c2))
# output
print(smash[row - 1][col - 1])