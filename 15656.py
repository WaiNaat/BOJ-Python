# function
def dfs(m):
	if len(seq) == m:
		print(*seq)
		return
	for num in numbers:
		seq.append(num)
		dfs(m)
		seq.pop()

# input
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
# process & output
numbers.sort()
seq = []
dfs(m)