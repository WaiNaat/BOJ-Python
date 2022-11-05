### 틀렸습니다 ###

'''
BFS
같은 턴에 불에 닿으면 죽으니까 불 먼저 움직인다
'''
import sys
from collections import deque
input = sys.stdin.readline

# input
R, C = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(R)]

# process
# 초기 위치 찾기
q_jihun = deque()
q_fire = deque()
for r in range(R):
    for c in range(C):
        if maze[r][c] == 'J':
            q_jihun.append((r, c, 0))
        elif maze[r][c] == 'F':
            q_fire.append((r, c))
            
# BFS
directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
sol = 'IMPOSSIBLE'

while q_jihun and q_fire:
    r_jihun, c_jihun, time = q_jihun.popleft()
    r_fire, c_fire = q_fire.popleft()

    # 불 이동
    for dr, dc in directions:
        r2 = r_fire + dr
        c2 = c_fire + dc

        if not 0 <= r2 < R or not 0 <= c2 < C or maze[r2][c2] == 'F' or maze[r2][c2] == '#':
            continue

        q_fire.append((r2, c2))
        maze[r2][c2] = 'F'

    # 지훈이 이동
    for dr, dc in directions:
        r2 = r_jihun + dr
        c2 = c_jihun + dc

        if not 0 <= r2 < R or not 0 <= c2 < C:
            sol = time + 1
            q_jihun = []
            break

        if maze[r2][c2] == '.':
            q_jihun.append((r2, c2, time + 1))
            maze[r2][c2] = 'J'

# output
print(sol)