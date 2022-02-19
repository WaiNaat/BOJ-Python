# function
def dfs(n, m):
	if len(seq) == m:
		print(*seq)
		return
	for num in numbers:
		if visited[num] == 0:
			seq.append(num)
			visited[num] = 1
			dfs(n, m)
			seq.pop()
			visited[num] = 0

# input
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
# process & output
numbers.sort()
visited = {val:0 for val in numbers}
seq = []
dfs(n, m)