import sys, heapq
input = sys.stdin.readline
# constant
INF = 1234567890
# input
n = int(input())
street = [tuple(map(int, input().split())) for _ in range(n)]
# process
'''
퇴근을 '빨리' 할 필요는 없음
slope(a, b)를 출발점부터 A(a, b)까지 오는 경로 중 최대 경사의 최솟값이라 하고
이걸 기준으로 다익스트라 알고리즘 사용.
'''
visited = [[0 for _ in range(n)] for _ in range(n)]

h = [(INF, i, j) for i in range(n) for j in range(n)]
h[0] = (0, 0, 0)
heapq.heapify(h)

slope = [[INF for _ in range(n)] for _ in range(n)]
slope[0][0] = 0

dir = ((1, 0), (-1, 0), (0, 1), (0, -1))
while h:
	min_slope, r, c = heapq.heappop(h)
	if r == c == n - 1: break
	if visited[r][c] == 1: continue
	visited[r][c] = 1
	# 상하좌우 탐색
	for dr, dc in dir:
		r2 = r + dr
		c2 = c + dc
		if not 0 <= r2 < n or not 0 <= c2 < n: continue
		if visited[r2][c2] == 1: continue
		# 현재 위치한 길에서 인접한 길까지의 경사 계산 후
		# 거기까지 가는 데 필요한 최대 경사값 계산
		next_slope = abs(street[r][c] - street[r2][c2])
		if next_slope < slope[r][c]:
			next_slope = slope[r][c]
		# 만약 이 경로를 따라 이동했을 때 최대 경사값이 줄어들면 반영
		if next_slope < slope[r2][c2]:
			slope[r2][c2] = next_slope 
			heapq.heappush(h, (slope[r2][c2], r2, c2))
# output
print(slope[n - 1][n - 1])