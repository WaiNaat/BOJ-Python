### 틀렸습니다 ###

'''
일단 주어진 선들 중 비싼거 k개를 0원으로 만든다.
다익스트라로 N번까지 연결하는 최소비용 및 경로를 구한다.
해당 경로에 0원인 선이 k개보다 적다면 k개가 되도록 추가 할인받는다.
	적다는 건 할인을 받았음에도 불구하고 N번까지 연결하는 데 하등 도움이 안된다는 뜻.
	이러면 그걸 할인 안받는다 하고 다른걸 할인받아도 다익스트라 결과에는 변함이 없음.


반례)
5 5 2
1 2 1000
1 3 1000
3 4 50
4 5 30
2 5 100

위의 풀이에 따르면 처음에 1000짜리 2개를 지우고
다익스트라로 비용 50의 1-3-4-5 루트를 고른 후 50을 제거하고 30을 답으로 제시.
하지만 실제 정답은 1-2-5 루트로 2개 모두 무료혜택 받아서 0원으로 설치가 가능함.

근데 밑에 코드는 50으로 답 내는걸 봐서는 구현자체에 문제가 있는듯?
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