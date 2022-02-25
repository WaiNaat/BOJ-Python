# function
def dfs(m):
	'''
	같은 depth에서 이미 골랐던 숫자는 고르면 안 됨
	예를 들어 1, 2, 2, 3이면
	첫번째 2를 골라서 2, 3이란 수열을 만들었으면
	두번째 2를 골라서 2, 3이란 수열을 만들면 안 됨.
		>> 숫자들은 정렬되어 있기 때문에
		바로 직전에 골랐던 숫자와 같은 숫자를 골랐다면 패스.
	'''
	if len(seq) == m:
		print(*seq)
		return
	
	prev = 0
	for i in range(n):
		if numbers[i] != prev and visited[i] == 0 \
			and (len(seq) == 0 or seq[-1] <= numbers[i]):
			visited[i] = 1
			seq.append(numbers[i])
			dfs(m)
			seq.pop()
			visited[i] = 0
			prev = numbers[i]			

# input
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
# process & output
numbers.sort()
seq = []
visited = [0 for _ in range(n)]
dfs(m)