### 시간 초과 ###

### pypy로 제출하면 맞긴 함 ###

'''
opt(start, end) := start번~end번 행렬 곱할때 최소 연산 횟수
opt(start, end) = min(opt(start, mid) + opt(mid + 1, end) + 두 덩어리 사이의 연산횟수)
재귀 + 메모이제이션으로 구현
'''
import sys
input = sys.stdin.readline

# function
def calculation_count(start, end):
	# base case
	if opt[start][end] < float('inf'):
		return opt[start][end]
	
	# recursive step
	for mid in range(start, end):
		val = calculation_count(start, mid)
		val += calculation_count(mid + 1, end)
		val += matrix[start][0] * matrix[mid][1] * matrix[end][1]		
		opt[start][end] = min(val, opt[start][end])

	return opt[start][end]

# input
N = int(input())
matrix = [tuple(map(int, input().split())) for _ in range(N)]

# process
opt = [[float('inf') for _ in range(N)] for _ in range(N)]

for k in range(N - 1):
	opt[k][k + 1] = matrix[k][0] * matrix[k][1] * matrix[k + 1][1]
	opt[k][k] = 0
opt[N - 1][N - 1] = 0

calculation_count(0, N - 1)

# output
print(opt[0][N - 1])