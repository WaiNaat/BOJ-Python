'''
BFS
3차원 visited배열 사용: (r, c, 벽 부순 횟수)
저장하는 값은 0이면 방문안함, 1이상이면 최단경로길이
'''
import sys
from collections import deque
input = sys.stdin.readline

# input
row, col = map(int, input().split())
area = [input().strip() for _ in range(row)]

# process
directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
visited = [[[0, 0] for _ in range(col)] for _ in range(row)]
q = deque([(0, 0, 1, 0)])
sol = -1

while q:
    r, c, move, smash = q.popleft()

    if r == row - 1 and c == col - 1:
        sol = move
        break
    elif visited[r][c][smash] > 0: continue
    visited[r][c][smash] = move

    for dr, dc in directions:
        r2 = r + dr
        c2 = c + dc

        if not 0 <= r2 < row or not 0 <= c2 < col: continue

        if smash == 0 and area[r2][c2] == '1' and visited[r2][c2][1] == 0:
            q.append((r2, c2, move + 1, 1))
        elif area[r2][c2] == '0' and visited[r2][c2][smash] == 0:
            q.append((r2, c2, move + 1, smash))

# output
print(sol)