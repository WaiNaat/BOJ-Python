'''
opt(i, j) := 원룡씨의 위치가 (i, j)일 때 최대 점수
score(i, j) := (i, j)칸에 적힌 점수
opt(i, j) = 
    opt(i-1, j-1)
    opt(i-1, j)
    opt(i-1, j+1)
    셋 중 제일 큰 값에 score(i, j)를 더한 값.

메모리 제한이 걸려있으니 각 줄마다 점수 입력받음과 동시에 계산.
'''
import sys
input = sys.stdin.readline

# constant
INF = 1234567

N = int(input())

cur_max = list(map(int, input().split()))
cur_min = [i for i in cur_max]

for _ in range(1, N):
    score = list(map(int, input().split()))

    next_max = [
        score[0] + max(cur_max[0], cur_max[1]),
        score[1] + max(cur_max[0], cur_max[1], cur_max[2]),
        score[2] + max(cur_max[1], cur_max[2])
    ]

    next_min = [
        score[0] + min(cur_min[0], cur_min[1]),
        score[1] + min(cur_min[0], cur_min[1], cur_min[2]),
        score[2] + min(cur_min[1], cur_min[2])
    ]

    cur_max = next_max
    cur_min = next_min

# output
print(max(cur_max), min(cur_min))