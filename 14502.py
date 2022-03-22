### python3 시간초과, pypy3 맞았습니다 ###

import sys
input = sys.stdin.readline
'''
dfs/bfs로 바이러스의 퍼짐 계산 가능.
    O(V+E)이고 max(|V|)=64니까 대략 계산 300회

연구소 최대크기가 64니까 벽 3개를 세우는 경우의 수는
64^3, 대략 22만 회 >> 이건 백트래킹으로 가능

총 계산 수는 약 6600만 회니까 2초면 완전탐색 가능

안전 영역 세는 건 바이러스 퍼지기 전 안전영역 개수에서
바이러스가 퍼진 칸 수 빼면 금방 계산 가능.
'''
# functions
def putWalls(wall_cnt):
    '''백트래킹으로 벽 3개 세우는 함수'''
    global sol, row, col, safe_cnt

    # base case
    if wall_cnt == 3:
        polluted = dfs(row, col)
        sol = max(sol, safe_cnt - polluted)
        return

    # recursive step
    for r in range(row):
        for c in range(col):
            if lab[r][c] == 0:
                lab[r][c] = 1
                putWalls(wall_cnt + 1)
                lab[r][c] = 0

def dfs(row, col):
    '''DFS로 바이러스가 오염시킨 안전영역 수 세는 함수'''
    visited = [line.copy() for line in lab]
    stack = virus_loc.copy()
    cnt = 0
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while stack:
        r, c = stack.pop()

        for dr, dc in directions:
            r2 = r + dr
            c2 = c + dc

            if not 0 <= r2 < row or not 0 <= c2 < col:
                continue

            if visited[r2][c2] == 0:
                cnt += 1
                visited[r2][c2] = 1
                stack.append((r2, c2))

    return cnt

# input
row, col = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(row)]

# process
# 초기 안전영역 수랑 바이러스 위치 계산
safe_cnt = -3 # 벽 3개 세울거라서 미리 빼놓음
virus_loc = []

for r in range(row):
    for c in range(col):
        if lab[r][c] == 0:
            safe_cnt += 1
        elif lab[r][c] == 2:
            virus_loc.append((r, c))

# 답 계산
sol = 0
putWalls(0)

# output
print(sol)