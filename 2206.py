'''
출발지부터 BFS
    도중에 벽을 만날 경우 해당 벽의 위치와 벽까지 가는 최단경로 길이를 기억
도착지부터 BFS
    각 위치부터 도착지까지 가는 최단경로 길이 확인
위에서 기억한 벽들의 사방을 확인하고 만약 도착지까지 가는 최단경로가 있으면 반영
'''
import sys
from collections import deque
input = sys.stdin.readline

# input
row, col = map(int, input().split())
area = [list(map(int, list(input().strip()))) for _ in range(row)]

# process
# 벽 찾기
visited = [[False for _ in range(col)] for _ in range(row)]
q = deque([(0, 0, 1)])
directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
walls = []

while q:
    r, c, move = q.popleft()

    if visited[r][c]: continue
    visited[r][c] = True

    for dr, dc in directions:
        r2 = r + dr
        c2 = c + dc

        if not 0 <= r2 < row or not 0 <= c2 < col or visited[r2][c2]: continue

        if area[r2][c2] == 1:
            walls.append((r2, c2, move + 1))
        else:
            q.append((r2, c2, move + 1))

# 최단경로 찾기
q = deque([(row - 1, col - 1, 1)])
while q:
    r, c, move = q.popleft()

    if area[r][c] < 0: continue
    area[r][c] = -move

    for dr, dc in directions:
        r2 = r + dr
        c2 = c + dc

        if not 0 <= r2 < row or not 0 <= c2 < col or area[r2][c2] != 0: continue

        if area[r2][c2] == 0:
            q.append((r2, c2, move + 1))

# 정답 계산
sol = float('inf') if area[0][0] == 0 else -area[0][0]

for r, c, move in walls:
    for dr, dc in directions:
        r2 = r + dr
        c2 = c + dc

        if not 0 <= r2 < row or not 0 <= c2 < col: continue

        if area[r2][c2] < 0:
            sol = min(move - area[r2][c2], sol)

# output
print(sol if sol < float('inf') else -1)