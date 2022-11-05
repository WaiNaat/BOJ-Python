'''
BFS
불들 먼저 찾아서 움직여봄 >> 미로에 언제 불이 번지는지 기록
지훈이 움직임 >> 불이 이미 번져있는곳으론 갈수없음
'''
import sys
from collections import deque
input = sys.stdin.readline

# input
R, C = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(R)]

# process
# 초기 위치 찾기
jihun = deque()
fire = deque()
for r in range(R):
    for c in range(C):
        if maze[r][c] == 'J':
            jihun.append((r, c, 0))
            maze[r][c] = '.'
        elif maze[r][c] == 'F':
            fire.append((r, c, 0))
            maze[r][c] = 0
            
# 불 이동
DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))
while fire:
    r, c, time = fire.popleft()
    for dr, dc in DIRECTIONS:
        r2 = r + dr
        c2 = c + dc

        if not 0 <= r2 < R or not 0 <= c2 < C: continue
        if maze[r2][c2] == '.':
            maze[r2][c2] = time + 1
            fire.append((r2, c2, time + 1))

# 지훈이 이동
sol = 'IMPOSSIBLE'
while jihun:
    r, c, time = jihun.popleft()
    for dr, dc in DIRECTIONS:
        r2 = r + dr
        c2 = c + dc

        if not 0 <= r2 < R or not 0 <= c2 < C:
            sol = time + 1
            jihun = []
            break
        if maze[r2][c2] == '#' or maze[r2][c2] == 'J': continue

        if maze[r2][c2] == '.' or time + 1 < maze[r2][c2]:
            maze[r2][c2] = 'J'
            jihun.append((r2, c2, time + 1))

# output
print(sol)