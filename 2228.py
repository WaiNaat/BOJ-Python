### 시간 초과 ###

'''
처음에 누적합배열을 만들어서 구간합 빠르게 계산
opt(cnt, start, end) := cnt번째 구간이 start~end일 떄 최대합
opt(cnt, start, end) := 
	opt(cnt-1, i, j) + partial_sum(start, end)
	0 <= i <= j, j + 1 < start 인 정수
'''
import sys
input = sys.stdin.readline

# input
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# process
acc_sum = [arr[0]]
for i in range(1, N):
	acc_sum.append(acc_sum[-1] + arr[i])

opt = [[[None for _ in range(N)] for _ in range(N)] for _ in range(M)]

for start in range(N):
	for end in range(start, N):
		opt[0][start][end] = acc_sum[end] - (acc_sum[start - 1] if start > 0 else 0)

for cnt in range(1, M):
	for start in range(N):
		for end in range(start, N):
			
			val = -float('inf')
			for j in range(start - 1):
				for i in range(j+1):
					val = max(val, opt[cnt - 1][i][j])
			opt[cnt][start][end] = val + acc_sum[end] - (acc_sum[start - 1] if start > 0 else 0)

# output
sol = -float('inf')
for start in range(N):
	for end in range(start, N):
		sol = max(sol, opt[M - 1][start][end])
print(sol)