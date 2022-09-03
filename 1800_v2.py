'''
다익스트라를 돌리는데
힙에 넣을떄 (비용, 위치)가 아니라
(비용, 공짜혜택받은횟수, 위치)를 넣는다.

즉 현재 위치에서 인접한 위치들로의 이동을 판단할 때
비용이 높아진다면 혜택받기/안받기를 선택해서 두 가지 경우를 넣는다.

visited 역시 단순히 해당 위치를 방문했는지가 아니라
위치와 혜택을 받은 횟수 두 가지가 일치하는 방문을 중복이라 처리한다.
'''
import sys, heapq
input = sys.stdin.readline

# constant
INF = 1234567

# input
N, P, K = map(int, input().split())
cables = [[] for _ in range(N + 1)]
for _ in range(P):
    pc1, pc2, cost = map(int, input().split())
    cables[pc1].append((pc2, cost))
    cables[pc2].append((pc1, cost))
    
# process
visited = [set() for _ in range(N + 1)]
h = [(0, 0, 1)]
sol = None

while h:
    cur_cost, cur_free_cnt, cur = heapq.heappop(h)
    
    if cur_free_cnt in visited[cur]: continue
    visited[cur].add(cur_free_cnt)

    if cur == N:
        sol = cur_cost
        break
    
    for next, cable_cost in cables[cur]:
        if cur_cost < cable_cost and cur_free_cnt < K and cur_free_cnt + 1 not in visited[next]:
            heapq.heappush(h, (cur_cost, cur_free_cnt + 1, next))
        if cur_free_cnt not in visited[next]:
            heapq.heappush(h, (max(cur_cost, cable_cost), cur_free_cnt, next))

# output
print(sol if len(visited[N]) > 0 else -1)