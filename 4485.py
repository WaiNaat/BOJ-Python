'''
다익스트라
'''
import sys, heapq
input = sys.stdin.readline

INF = 12345678
directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
problem = 0
sol = []

while True:
    N = int(input())
    if N == 0: break
    cave = [tuple(map(int, input().split())) for _ in range(N)]

    lose = [[INF for _ in range(N)] for _ in range(N)]
    lose[0][0] = cave[0][0]

    visited = [[False for _ in range(N)] for _ in range(N)]

    h = [(cave[0][0], 0, 0)]

    while h:
        cost, r, c = heapq.heappop(h)

        if visited[r][c]: continue
        visited[r][c] = True

        if r == N - 1 and c == N - 1:
            problem += 1
            sol.append(f'Problem {problem}: {lose[N - 1][N - 1]}')

        for dr, dc in directions:
            r2 = r + dr
            c2 = c + dc

            if not 0 <= r2 < N or not 0 <= c2 < N or visited[r2][c2]:
                continue
            
            if cost + cave[r2][c2] < lose[r2][c2]:
                heapq.heappush(h, (cost + cave[r2][c2], r2, c2))
                lose[r2][c2] = cost + cave[r2][c2]

print('\n'.join(sol))