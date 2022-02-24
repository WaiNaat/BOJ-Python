### 시간 초과 ###

# function
def dfs(n, m):
	'''
	출력할 때마다 prev에 저장된 이전 출력값들과 비교해서
	같은 게 있으면 출력하지 않음
	'''
	if len(seq) == m:
		if seq not in prev:
			prev.append(seq.copy())
			print(*seq)
		return

	for i in range(n):
		if visited[i] == 0:
			visited[i] = 1
			seq.append(numbers[i])
			dfs(n, m)
			seq.pop()
			visited[i] = 0

# input
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
# process & output
seq = []
prev = []
visited = [0 for _ in range(n)]
numbers.sort()
dfs(n, m)