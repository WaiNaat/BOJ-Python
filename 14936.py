'''
각 구역마다 본인을 시작점으로 하는 다익스트라를 돌린다.
'''
import sys, heapq
input = sys.stdin.readline

# constant
INF = 12345678

# input
n, search_range, r = map(int, input().split())
item = tuple(map(int, input().split()))
road = [[] for _ in range(n)]
for _ in range(r):
    a, b, l = map(int, input().split())
    a -= 1
    b -= 1
    road[a].append((b, l))
    road[b].append((a, l))

# process
sol = 0

for start in range(n):
    visited = [False for _ in range(n)]
    dist = [INF for _ in range(n)]

    item_cnt = 0
    h = [(0, start)]
    dist[start] = 0
    
    while h:
        d, cur = heapq.heappop(h)

        if d > search_range:
            break

        if visited[cur]: continue
        visited[cur] = True
        item_cnt += item[cur]

        for next, l in road[cur]:
            if not visited[next] and d + l < dist[next]:
                dist[next] = d + l
                heapq.heappush(h, (d + l, next))
                
    sol = max(item_cnt, sol)

# output
print(sol)