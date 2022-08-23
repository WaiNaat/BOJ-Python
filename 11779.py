'''
다익스트라
prev 배열을 추가로 만들어서 경로 역추적
'''
import sys, heapq
input = sys.stdin.readline

# constant
INF = 100000 ** 2 + 1

# input
city_num = int(input())
bus_num = int(input())
bus_info = [[] for _ in range(city_num + 1)]
for _ in range(bus_num):
    start, end, cost = map(int, input().split())
    bus_info[start].append((end, cost))
start, end = map(int, input().split())

# process
# 다익스트라
cost = [INF for _ in range(city_num + 1)]
prev = [-1 for _ in range(city_num + 1)]
visited = [False for _ in range(city_num + 1)]
h = [(0, start)]

cost[start] = 0

while h:
    _, cur = heapq.heappop(h)

    if cur == end: break

    if visited[cur]: continue
    visited[cur] = True

    for bus_end, bus_cost in bus_info[cur]:
        if cost[cur] + bus_cost < cost[bus_end]:
            cost[bus_end] = cost[cur] + bus_cost
            prev[bus_end] = cur
            heapq.heappush(h, (cost[bus_end], bus_end))

# 경로 역추적
cnt = 0
path = []
cur = end

while cur != -1:
    path.append(cur)
    cur = prev[cur]
    cnt += 1

path.reverse()

# output
print(f"{cost[end]}\n{cnt}")
print(*path)