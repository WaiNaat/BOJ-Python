### 틀렸습니다 ###

'''
처음에 누적합배열을 만들어서 구간합 빠르게 계산

opt(cnt, i) := i개의 숫자로 cnt개의 구간을 만들었을 떄 최대합
opt(cnt, i) = 
	opt(cnt-1, i-2) + arr[i] (새로운 구간 만들기)
	opt(cnt, i-1) + arr[i] (이전 구간에 끼워붙이기)
	opt(cnt, i-1)
	셋 중 가장 큰 값
'''
import sys
input = sys.stdin.readline

# input
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# process
opt = [[None for _ in range(N)] for _ in range(M)]

for cnt in range(M):
	for i in range(cnt * 2, N):
		opt[cnt][i] = max(
			(opt[cnt - 1][i - 2] if cnt > 0 and i > max(1, cnt * 2) else 0) + arr[i],
			(opt[cnt][i - 1] if i > cnt * 2 else 0) + arr[i],
			opt[cnt][i - 1] if i > cnt * 2 else -float('inf')
		)
		
# output
print(opt[M - 1][N - 1])