'''
다익스트라
검은방으로 이동할 때 비용 1
흰방으로 이동할 때 비용 0
'''
import sys, heapq
input = sys.stdin.readline

# constants
INF = 7777
DIRECTIONS = ((-1, 0), (1, 0), (0, 1), (0, -1))

# input
N = int(input())
room = [tuple(map(lambda x: 1 if x == '0' else 0, input().rstrip())) for _ in range(N)]

# process
visited = [[False for _ in range(N)] for _ in range(N)]
cost = [[INF for _ in range(N)] for _ in range(N)]

cost[0][0] = 0
h = [(0, 0, 0)]

while h:
    cur_cost, r, c = heapq.heappop(h)

    if r == N - 1 and c == N - 1:
        break

    if visited[r][c]: continue
    visited[r][c] = True

    for dr, dc in DIRECTIONS:
        r2 = r + dr
        c2 = c + dc

        if not 0 <= r2 < N or not 0 <= c2 < N or visited[r2][c2]:
            continue

        if cur_cost + room[r2][c2] < cost[r2][c2]:
            cost[r2][c2] = cur_cost + room[r2][c2]
            heapq.heappush(h, (cost[r2][c2], r2, c2))

# output
print(cost[N - 1][N - 1])