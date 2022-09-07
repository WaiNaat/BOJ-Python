### 메모리 초과 ###

'''
opt(i, j) := 원룡씨의 위치가 (i, j)일 때 최대 점수
score(i, j) := (i, j)칸에 적힌 점수
opt(i, j) = 
    opt(i-1, j-1)
    opt(i-1, j)
    opt(i-1, j+1)
    셋 중 제일 큰 값에 score(i, j)를 더한 값.

메모리 제한이 걸려있고 opt(i, ?) 계산에 opt(i-1, ?)만 필요하니
prev, cur 두 개의 일차원 배열로 해결
'''
import sys
input = sys.stdin.readline

# constant
INF = 1234567

# input
N = int(input())
score = [list(map(int, input().split())) for _ in range(N)]

# process
prev_max = [score[0][i] for i in range(N)]
prev_min = [score[0][i] for i in range(N)]

for r in range(1, N):
    cur_max = [score[r][c] + max(
        prev_max[c - 1] if c > 0 else 0,
        prev_max[c],
        prev_max[c + 1] if c < N - 1 else 0
    ) for c in range(N)]

    cur_min = [score[r][c] + min(
        prev_min[c - 1] if c > 0 else INF,
        prev_min[c],
        prev_min[c + 1] if c < N - 1 else INF
    ) for c in range(N)]

    prev_max = cur_max
    prev_min = cur_min

# output
print(max(prev_max), min(prev_min))