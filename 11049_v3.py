### 시간 초과 ###

'''
opt(start, end) := start번~end번 행렬 곱할때 최소 연산 횟수
opt(start, end) = min(opt(start, mid) + opt(mid + 1, end) + 두 덩어리 사이의 연산횟수)

opt배열을 채우는 순서
구간이 좁은 순서부터 채움
'''
import sys
input = sys.stdin.readline

# input
N = int(input())
matrix = [tuple(map(int, input().split())) for _ in range(N)]

# process
opt = [[float('inf') for _ in range(N)] for _ in range(N)]

for k in range(N):
	opt[k][k] = 0

for length in range(2, N + 1):
	for start in range(N):
		end = start + length - 1
		if end >= N: continue

		for mid in range(start, end):
			opt[start][end] = min(
				opt[start][mid] + opt[mid + 1][end] + matrix[start][0] * matrix[mid][1] * matrix[end][1],
				opt[start][end]
			)

# output
print(opt[0][N - 1])