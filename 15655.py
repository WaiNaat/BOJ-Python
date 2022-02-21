# function
def dfs(n, m):
	if len(seq) == m:
		print(*seq)
		return
	for num in numbers:
		if visited[num] == 0 and (len(seq) == 0 or seq[-1] < num):
			visited[num] = 1
			seq.append(num)
			dfs(n, m)
			seq.pop()
			visited[num] = 0

# input
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
# process & output
seq = []
visited = {i:0 for i in numbers}
numbers.sort()
dfs(n, m)