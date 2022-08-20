'''
S와 K에서 복제 가능 >> 각 K는 본인이랑 가장 가까운 S 또는 K부터 출발해서 오는게 이득

정점을 S와 K로 하고
간선의 비용을 (bfs로 찾은) 다른 S 또는 K와의 거리로 하는 그래프
이 그래프에서 크루스칼 알고리즘으로 mst를 찾는다
'''
import sys
from collections import deque
input = sys.stdin.readline

# constant
directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

# functions
def bfs(r, c):
    q = deque([(r, c, 0)])
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[r][c] = True
    this = (r, c)
    
    while q:
        r, c, d = q.popleft()

        if (maze[r][c] == 'S' or maze[r][c] == 'K') and d > 0:
            E.append((this, (r, c), d))

        for dr, dc in directions:
            r2 = r + dr
            c2 = c + dc

            if not 0 < r2 < N - 1 or not 0 < c2 < N - 1 or maze[r2][c2] == '1' or visited[r2][c2]:
                continue
            
            visited[r2][c2] = True
            q.append((r2, c2, d + 1))

def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

# input
N, M = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(N)]

# process
# 각 정점별로 bfs 수행
E = []
parent = {}

for r in range(N):
    for c in range(N):
        if maze[r][c] == 'S' or maze[r][c] == 'K':
            parent[(r, c)] = (r, c)
            bfs(r, c)

# 크루스칼 알고리즘
E.sort(key = lambda x: x[2])

sol = 0
edge_cnt = 0

for v1, v2, w in E:
    if edge_cnt == M:
        break

    if find(v1) != find(v2):
        union(v1, v2)
        sol += w
        edge_cnt += 1
        
# output
print(sol if edge_cnt == M else -1)