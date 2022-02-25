# function
def dfs(m):
	if len(seq) == m:
		print(' '.join(map(str, seq)))
		return
	
	for num in numbers:
		if len(seq) == 0 or seq[-1] <= num:
			seq.append(num)
			dfs(m)
			seq.pop()

# input
n, m = map(int, input().split())
numbers = map(int, input().split())

# process & output
'''
n과 m 11번과 마찬가지로 같은 수 고르기가 되기 때문에
처음에 주어진 n개의 자연수들에서 중복수를 제거한 다음 백트래킹.
'''
numbers = sorted(list(set(numbers)))
seq = []
dfs(m)