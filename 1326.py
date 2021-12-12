from collections import deque

# functions
def BFS(start, end, N):
	if start == end: return 0

	visited = [-1 for _ in range(N)]
	q = deque([])

	visited[start] = 0
	q.append(start)
	while q:
		'''
		stone := 현재 개구리 위치
		step := 개구리가 여태까지 몇 번 이동했는지
		val := 현재 징검다리에 써 있는 숫자
		adj := 인접 vertex (이동가능한 징검다리 번호)
		'''
		stone = q.popleft()
		step = visited[stone]
		val = values[stone]
		# 오른쪽으로 이동하는 경우
		for adj in range(stone+val, N, val):
			if visited[adj] == -1:
				visited[adj] = step + 1
				if adj == end: return visited[adj]
				q.append(adj)
		# 왼쪽으로 이동하는 경우
		for adj in range(stone-val, -1, -val):
			if visited[adj] == -1:
				visited[adj] = step + 1
				if adj == end: return visited[adj]
				q.append(adj)

	return -1

# input
N = int(input())
values = tuple(map(int, input().split()))
a, b = map(int, input().split())

# process & output
print(BFS(a - 1, b - 1, N))