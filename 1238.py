import sys, heapq
input = sys.stdin.readline

# constant
INF = 1234567

# function
def dijkstra(n, x, road):
	visited = [False for _ in range(n + 1)]

	time = [INF for _ in range(n + 1)]
	time[x] = 0

	h = [(INF, i) for i in range(1, n + 1)]
	h.append((0, x))
	heapq.heapify(h)

	while h:
		_, cur = heapq.heappop(h)

		if visited[cur]: continue
		visited[cur] = True

		for next, t in road[cur]:
			if time[cur] + t < time[next]:
				time[next] = time[cur] + t
				heapq.heappush(h, (time[next], next))
	
	return time

# input
n, m, x = map(int, input().split())
road1 = [[] for _ in range(n + 1)]
road2 = [[] for _ in range(n + 1)]
for _ in range(m):
	start, end, t = map(int, input().split())
	road1[end].append((start, t))
	road2[start].append((end, t))

# process
'''
다익스트라 알고리즘 두 번 사용.
1. 처음에 파티장에 모일 때:
	출발지를 X번 마을로 하고 X번 마을에서 각 마을까지 최단거리 구함.
	>> 길은 단방향이므로 입력받을 때 거꾸로 받아야 함.
2. 파티장에서 집으로 갈 때:
	출발지를 X번 마을로 하고 X번 마을에서 각 마을까지 최단거리 구함.
'''
time1 = dijkstra(n, x, road1)
time2 = dijkstra(n, x, road2)
total_time = [time1[i] + time2[i] for i in range(1, n + 1)]

# output
print(max(total_time))