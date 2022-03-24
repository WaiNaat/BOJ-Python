import sys
input = sys.stdin.readline

# function
def DFS(r, c, n, rain):
    stack = [(r, c)]

    while stack:
        r, c = stack.pop()

        for dr, dc in directions:
            r2 = r + dr
            c2 = c + dc

            if not 0 <= r2 < n or not 0 <= c2 < n:
                continue

            if area[r2][c2] > rain and visited[r2][c2] == 0:
                visited[r2][c2] = 1
                stack.append((r2, c2))

# input
n = int(input())
area = [tuple(map(int, input().split())) for _ in range(n)]

# process
'''
구역 세기는 bfs/dfs로 쉽게 구할 수 있다. O(V+E)=대략 5만?
높이는 100가지 경우의 수가 있으므로 완전탐색 가능.
'''
sol = 1
rain = 1
safe = 1
directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

while safe > 0 and rain <= 100:

    # 초기화
    safe = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]

    # 비에 잠기지 않는 곳을 고른다.
    for r in range(n):
        for c in range(n):

            if area[r][c] > rain and visited[r][c] == 0:
                safe += 1
                DFS(r, c, n, rain)
    
    # 정답 업데이트
    sol = max(sol, safe)
    rain += 1

# output
print(sol)