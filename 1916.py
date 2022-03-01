import sys, heapq
input = sys.stdin.readline

# constant
INF = 1234567890

# input
n = int(input())
m = int(input())
city = [[] for _ in range(n + 1)]
for _ in range(m):
	start, end, cost = map(int, input().split())
	city[start].append((end, cost))
start, end = map(int, input().split())

# process
'''
다익스트라 알고리즘 사용
'''
visited = [False for _ in range(n + 1)]

h = [(INF, i) for i in range(1, n + 1)]
h.append((0, start))
heapq.heapify(h)

cost = [INF for _ in range(n + 1)]
cost[start] = 0

while h:
	_, cur = heapq.heappop(h)

	if cur == end: break
	if visited[cur]: continue

	visited[cur] = True

	for next, c in city[cur]:
		if cost[cur] + c < cost[next]:
			cost[next] = cost[cur] + c
			heapq.heappush(h, (cost[next], next))

# output
print(cost[end])