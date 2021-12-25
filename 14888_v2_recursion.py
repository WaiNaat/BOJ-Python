# functions
div = lambda a, b: -(-a//b) if a<0 else a//b

def DFS(add, sub, mult, divi, cur, result):
	'''
	add, sub, mult, divi := 각 연산자의 남은 사용 가능 횟수
	cur := 현재 연산에 사용되어야 할 수열 숫자의 index
	result := 현재까지의 계산 결과
	'''
	global result_max
	global result_min
	if add + sub + mult + divi == 0: # 모든 연산자 소진
		result_max = max(result_max, result)
		result_min = min(result_min, result)
		return

	if add > 0:
		DFS(add - 1, sub, mult, divi, cur + 1, result + A[cur])
	if sub > 0:
		DFS(add, sub - 1, mult, divi, cur + 1, result - A[cur])
	if mult > 0:
		DFS(add, sub, mult - 1, divi, cur + 1, result * A[cur])
	if divi > 0:
		DFS(add, sub, mult, divi - 1, cur + 1, div(result, A[cur]))

# input
N = int(input())
A = tuple(map(int, input().split()))
add, sub, mult, divi = map(int, input().split())
# process
'''
DFS를 이용한 완전탐색
'''
result_max = -1000000001
result_min = 1000000001
DFS(add, sub, mult, divi, 1, A[0])
# output
print(result_max)
print(result_min)