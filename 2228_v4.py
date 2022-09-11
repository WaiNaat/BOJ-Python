### 틀렸습니다 ###

'''
처음에 누적합을 만들어서 구간합 빠르게 계산

opt(cnt, i) := i개의 숫자로 cnt개의 구간을 만들었을 떄 최대합
opt(cnt, i) = 
    opt(cnt-1, k-2) + partial_sum(k, i)  (마지막 구간에 i번째 숫자를 쓰는 경우)
        단, k <= i
    opt(cnt, i-1) (i번째 숫자 안쓰기)
    중 가장 큰 값
'''
import sys
input = sys.stdin.readline

# input
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# process
for i in range(1, N):
    arr[i] += arr[i - 1]

opt = [[-float('inf') for _ in range(N)] for _ in range(M)]

for cnt in range(M):
    for i in range(N):
        if i > 0:
             opt[cnt][i] = opt[cnt][i - 1]

        for k in range(max(1, cnt * 2), i + 1):
            opt[cnt][i] = max((opt[cnt - 1][k - 2] if cnt > 0 and k > 2 else 0) + arr[i] - arr[k - 1], opt[cnt][i])
            
# output
print(opt[M - 1][N - 1])