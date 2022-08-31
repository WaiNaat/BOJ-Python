'''
순수 구현 문제
'''
import sys
input = sys.stdin.readline

# constant
DIRECTIONS = (None, (0, 1), (0, -1), (-1, 0), (1, 0))
RED = 1
BLUE = 2

# functions
def get_piece_pos(x):
    for r in range(N):
        for c in range(N):
            if board[r][c] and board[r][c][0][0] == x:
                return r, c
    return None, None

def change_direction(d):
    if d == 1: return 2
    elif d == 2: return 1
    elif d == 3: return 4
    else: return 3

def move(r, c):
    d = board[r][c][0][1]
    dr, dc = DIRECTIONS[d]

    r2 = r + dr
    c2 = c + dc

    # 파란색 또는 체스판 바깥
    if not 0 <= r2 < N or not 0 <= c2 < N or color[r2][c2] == BLUE:
        d = change_direction(d)

        board[r][c][0][1] = d
        dr, dc = DIRECTIONS[d]

        r2 = r + dr
        c2 = c + dc

        if not 0 <= r2 < N or not 0 <= c2 < N or color[r2][c2] == BLUE:
            return False
            
    # 빨간색이면 뒤집고 이동
    if color[r2][c2] == RED:
        board[r][c].reverse()

    board[r2][c2] += board[r][c]
    board[r][c] = []

    return True if len(board[r2][c2]) >= 4 else False


# input
N, K = map(int, input().split())
color = [tuple(map(int, input().split())) for _ in range(N)]
board = [[[] for _ in range(N)] for _ in range(N)]
id = 0
for _ in range(K):
    r, c, d = map(int, input().split())
    id += 1
    board[r - 1][c - 1].append([id, d])

# process
turn = 1
while turn <= 1000:
    isEnd = False

    for id in range(1, K + 1):
        r, c = get_piece_pos(id)
        if r is None: continue
        isEnd = move(r, c)
        if isEnd: break

    if isEnd: break
    turn += 1

# output
print(turn if turn <= 1000 else -1)