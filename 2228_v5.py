'''
처음에 누적합을 만들어서 구간합 빠르게 계산

opt(cnt, i) := i개의 숫자로 cnt개의 구간을 만들었을 때 최대합
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
prefix_sum = [0]
for val in arr:
    prefix_sum.append(prefix_sum[-1] + val)
    
opt = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for cnt in range(1, M + 1):
    opt[0][cnt] = -float('inf')

for i in range(1, N + 1):
    for cnt in range(1, M + 1):
        opt[i][cnt] = opt[i - 1][cnt]

        for k in range(1, i + 1):
            if k > 1:
                opt[i][cnt] = max(opt[k - 2][cnt - 1] + prefix_sum[i] - prefix_sum[k - 1], opt[i][cnt])
            elif cnt == 1 and k == 1:
                opt[i][cnt] = max(prefix_sum[i], opt[i][cnt])
            
# output
print(opt[N][M])