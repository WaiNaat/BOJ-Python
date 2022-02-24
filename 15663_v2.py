# function
def dfs(n, m):
	if len(seq) == m:
		sequences.append(seq.copy())
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

# process
'''
일단 같은 수열이라도 괜찮으니 모든 수열을 만든 후에
그 수열들을 사전순으로 정렬,
출력할 때 바로 직전 출력값과 같은 수열이면 출력하지 않음.
'''
seq = []
sequences = []
visited = [0 for _ in range(n)]
dfs(n, m)
sequences.sort()

# output
prev = []
for seq in sequences:
	if prev != seq:
		print(*seq)
	prev = seq.copy()