### 틀렸습니다 ###

'''
BFS
같은 턴에 불에 닿으면 죽으니까 불 먼저 움직인다
지훈이는 한 명이지만 불은 있을 수도 있고 없을 수도 있고 여러개일 수도 있음
'''
import sys
input = sys.stdin.readline

# constants
JIHUN = 0
FIRE = 1
DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))

# function
def move(r, c, type, q, R, C):
    for dr, dc in DIRECTIONS:
        r2 = r + dr
        c2 = c + dc

        if type == JIHUN:
            if not 0 <= r2 < R or not 0 <= c2 < C:
                return True
            if maze[r2][c2] == '.':
                q.append((r2, c2))
                maze[r2][c2] = 'J'
        else:
            if not 0 <= r2 < R or not 0 <= c2 < C or maze[r2][c2] == 'F' or maze[r2][c2] == '#':
                continue
            q.append((r2, c2))
            maze[r2][c2] = 'F'
    
    return False

# input
R, C = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(R)]

# process
# 초기 위치 찾기
jihun = []
fire = []
for r in range(R):
    for c in range(C):
        if maze[r][c] == 'J':
            jihun.append((r, c))
        elif maze[r][c] == 'F':
            fire.append((r, c))
            
# BFS
can_escape = False
turn = 0

while True:
    turn += 1
    next_fire = []
    next_jihun = []

    for r, c in fire:
        can_escape = move(r, c, FIRE, next_fire, R, C)
    
    for r, c in jihun:
        can_escape = move(r, c, JIHUN, next_jihun, R, C)

    if not next_jihun or can_escape: break

    jihun = next_jihun
    fire = next_fire

# output
print(turn if can_escape else 'IMPOSSIBLE')