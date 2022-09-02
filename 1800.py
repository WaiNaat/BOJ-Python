### 틀렸습니다 ###

'''
문제가 뭐냐면
100번 컴퓨터까지 연결해야 하고 1개의 선이 무료라고 하면
1 -> 2 -> ... -> 100으로 비용 100 나오고 할인받아서 99되는것보다
1 -> 100으로 바로 가는 비용 99999짜리 하나가 있다면 그거 고르는게 더 싸다는거

이러면 결국 다익스트라를 못쓰는거 아닌가?

일단 주어진 선들 중 비싼거 k개를 0원으로 만든다.
다익스트라로 N번까지 연결하는 최소비용 및 경로를 구한다.
해당 경로에 0원인 선이 k개보다 적다면 k개가 되도록 추가 할인받는다.
	적다는 건 할인을 받았음에도 불구하고 N번까지 연결하는 데 하등 도움이 안된다는 뜻.
	이러면 그걸 할인 안받는다 하고 다른걸 할인받아도 다익스트라 결과에는 변함이 없음.
'''
import sys, heapq
input = sys.stdin.readline

# constant
MAX = 1234567

# input
N, P, K = map(int, input().split())
cable_list = [list(map(int, input().split())) for _ in range(P)]

# process
# 비싼 k개의 선 할인
cable_list.sort(key = lambda x: -x[2])
for i in range(K):
	cable_list[i][2] = 0

# 인접 배열 만들기
cables = [[] for _ in range(N + 1)]
for a, b, cost in cable_list:
	cables[a].append((b, cost))
	cables[b].append((a, cost))

# 다익스트라
h = [(0, 1)]
cost = [MAX for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
prev = [-1 for _ in range(N + 1)]

while h:
	cur_cost, cur = heapq.heappop(h)

	if visited[cur]: continue
	visited[cur] = True

	if cur == N:
		break

	for next, cable_cost in cables[cur]:
		if not visited[next] and max(cur_cost, cable_cost) < cost[next]:
			cost[next] = max(cur_cost, cable_cost)
			prev[next] = cur
			heapq.heappush(h, (cost[next], next))

#  경로에 사용된 선의 비용 역추적
sol = -1
if visited[N]:
	cable_cnt = 0
	cur = N

	while cur != -1:
		cable_cnt += 1
		cur = prev[cur]
	
	cable_cnt -= 1

	# 추가 할인 가능 여부 확인
	if cable_cnt <= K:
		sol = 0
	else:
		sol = cost[N]

# output
print(sol)