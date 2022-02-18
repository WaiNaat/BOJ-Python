# function
def dfs(n, m, depth):
	# m개의 숫자를 다 반영했으면 출력
	if depth == m:
		print(*seq)
		return
	# 수열의 길이가 m이 안 되면 다음 숫자를 수열에 추가
	for i in range(1, n + 1):
		seq[depth] = i
		dfs(n, m, depth + 1)		
	
# input
n, m = map(int, input().split())
# process & output
seq = [None for _ in range(m)]
dfs(n, m, 0)