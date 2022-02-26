import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# function
def dfs(n):
	if len(reverse_string) == n:
		# 탐색 순서상 리버스 문자열은 오름차순으로 확인하고,
		# 사전 순서가 지켜지는 경우에만 dfs로 추가 탐색을 하고,
		# 항상 정답이 존재하기 때문에
		# 여기까지 왔으면 무조건 정답임.
		return True
	
	# 리버스하지 않은 경우와 리버스한 경우 두 가지를 탐색하되
	# 사전 순서가 지켜지지 않는 경우는 탐색하지 않음.
	# 1. 리버스하지 않은 경우
	if len(seq) == 0 or seq[-1] <= S[len(seq)]:
		seq.append(S[len(seq)])
		reverse_string.append(0)
		if dfs(n): return True
		reverse_string.pop()
		seq.pop()
	# 2. 리버스한 경우
	if len(seq) == 0 or seq[-1] <= S[len(seq)][::-1]:
		seq.append(S[len(seq)][::-1])
		reverse_string.append(1)
		if dfs(n): return True
		reverse_string.pop()
		seq.pop()

	return False


# input
t = int(input())
for _ in range(t):
	n = int(input())
	S = [input().rstrip() for _ in range(n)]

# process
	'''
	백트래킹으로 000...00, 000...01, 000...10, 000...11, ...
	순으로 탐색해야 함.
		>> 백트래킹 중 정답 찾으면 즉시 탈출 가능

	seq := 사전순으로 정렬중인 문자열들
	reverse_string := 계산된 리버스 문자열
	'''
	seq = []
	reverse_string = []
	dfs(n)

# output
	print(''.join(map(str, reverse_string)))