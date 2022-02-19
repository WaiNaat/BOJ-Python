import sys
sys.setrecursionlimit(10 ** 6)
# function
def dfs(n, m):
	if len(seq) == m:
		print(*seq)
		return
	for i in range(1, n + 1):
		if len(seq) == 0 or seq[-1] <= i:
			seq.append(i)
			dfs(n, m)
			seq.pop()

# input
n, m = map(int, input().split())
# process & output
seq = []
dfs(n, m)