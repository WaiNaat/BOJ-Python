import sys
from collections import deque
input = sys.stdin.readline
'''
BFS를 쓰면 초 단위로 바이러스 퍼지는거 파악 가능
각 바이러스별로 다음 단위시간에 퍼질 구역들을 저장할 배열 필요.
'''
# function
def bfs(N, S):
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    time_table = [[0 for _ in range(N)] for _ in range(N)]

    while virus:
        r, c, virus_name, time = virus.popleft()

        if time >= S: break

        for dr, dc in directions:
            r2 = r + dr
            c2 = c + dc

            if not 0 <= r2 < N or not 0 <= c2 < N:
                continue

            if test_tube[r2][c2] == 0 \
                or (test_tube[r2][c2] > virus_name and time_table[r2][c2] == time + 1):
                test_tube[r2][c2] = virus_name
                time_table[r2][c2] = time + 1
                virus.append((r2, c2, virus_name, time + 1))

# input
N, K = map(int, input().split())
test_tube = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

# process
# 바이러스 초기 위치 저장
virus = deque()
for r in range(N):
    for c in range(N):
        if test_tube[r][c] != 0:
            virus.append((r, c, test_tube[r][c], 0))

# 바이러스 확산
bfs(N, S)

# output
print(test_tube[X - 1][Y - 1])