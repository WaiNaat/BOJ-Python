# function
def dfs(n, m, depth):
	# base case
	if depth == m:
		print(*seq)
		return
	# recursive step
	for next in range(1, n + 1):
		# 다음 숫자는 방문한 숫자가 아니어야 하고
		# 이전 숫자보다 커야 한다.
		if visited[next] == 0 and (depth == 0 or seq[depth - 1] < next):
			visited[next] = 1
			seq[depth] = next
			dfs(n, m, depth + 1)
			visited[next] = 0

# input
n, m = map(int, input().split())
# process & output
visited = [0 for _ in range(n + 1)]
seq = [None for _ in range(m)]
dfs(n, m, 0)