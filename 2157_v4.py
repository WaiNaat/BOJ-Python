'''
opt(i, cnt) := 현위치가 i도시이고 총 지난 도시가 cnt개일 때 최대 점수
airway(i, j) := i도시 출발, j도시 도착 비행기의 기내식 점수
opt(i, cnt) = 
    max(opt(k, cnt-1) + airway(k, i)), k<i이고 k-i 항로가 있고 k>1이면 opt(k, cnt-1)>0
    opt(i, cnt-1), 그냥 안움직임
'''
import sys
input = sys.stdin.readline

# input
N, M, K = map(int, input().split())
airway = [{} for _ in range(N + 1)]
for _ in range(K):
    start, end, score = map(int, input().split())
    if start < end:
        airway[end][start] = max(score, airway[end][start] if start in airway[end] else 0)

# process
cur = [0 for _ in range(N + 1)]

for cnt in range(2, M + 1):
    next = cur[:]

    for end in range(2, N + 1):
        for start in airway[end].keys():
            if start > 1 and cur[start] == 0:
                continue
            next[end] = max(cur[start] + airway[end][start], next[end])

    cur = next

# output
print(cur[N])