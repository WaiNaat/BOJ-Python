import sys
sys.setrecursionlimit(10 ** 6)

# function
def dfs(n, m, depth):
	if depth == m:
		print(*seq)
		return
	
	for i in range(1, n + 1):
		if visited[i] == 0:
			visited[i] = 1
			seq[depth] = i
			dfs(n, m, depth + 1)
			visited[i] = 0

# input
n, m = map(int, input().split())
# process & output
visited = [0 for _ in range(n + 1)]
seq = [None for _ in range(m)]
seq[0] = 1

dfs(n, m, 0)