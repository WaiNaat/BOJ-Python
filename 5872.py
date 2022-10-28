'''
다익스트라 문제
'''
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

# input
N, M = map(int, input().split())
E = [[] for _ in range(N + 1)]
for _ in range(M):
	a, b, c = map(int, input().split())
	E[a].append((b, c))
	E[b].append((a, c))

# process
h = []
cost = [float('inf') for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

heappush(h, (0, 1))
cost[1] = 0

while h:
	cur_cost, cur = heappop(h)

	if cur == N: break

	if visited[cur]: continue
	visited[cur] = True

	for next, road_cost in E[cur]:
		if not visited[next] and cur_cost + road_cost < cost[next]:
			heappush(h, (cur_cost + road_cost, next))
			cost[next] = cur_cost + road_cost

# output
print(cost[N])