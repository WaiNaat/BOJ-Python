### 시간 초과 ###

'''
결국 어떤 한 도시부터 출발해서 하나의 큰 원형 경로를 만드는거니까
일단 출발도시는 0번 도시로 정해도 아무 문제 없음

백트래킹에 dp를 곁들여 시간 단축하는 문제
opt(현재도시, 방문한도시들) := 앞으로 여행하는데 드는 비용
opt(현재도시, 방문한도시들) = 
	opt(인접도시, 방문한도시들+인접도시)
	이것들 중 최솟값.

max(N)=16이므로 어떤 도시를 방문했는지 아닌지는 16비트 숫자로 표현이 가능함.
즉 opt배열의 크기는 일단 (N, 2^N).
'''
import sys
input = sys.stdin.readline

# function
def travel(cur, visited, N, VISITED_ALL):	
	# base case
	if opt[cur][visited] is not None:
		return opt[cur][visited]
	# 모든 도시를 방문했음
	elif visited == VISITED_ALL and travel_cost[cur][0] > 0: 
		opt[cur][visited] = travel_cost[cur][0]
		return opt[cur][visited]

	# recursive step
	candidates = []
	for next in range(N):
		# 길이 있는지 확인
		if travel_cost[cur][next] == 0:
			continue

		# 방문하지 않았는지 확인
		if ((VISITED_ALL - (1 << next)) | visited) == VISITED_ALL:
			continue

		val = travel(next, visited | (1 << next), N, VISITED_ALL)
		if val is not None: candidates.append(val + travel_cost[cur][next])
	
	if candidates:
		opt[cur][visited] = min(candidates)
	return opt[cur][visited]

# input
N = int(input())
travel_cost = [tuple(map(int, input().split())) for _ in range(N)]

# process
opt = [[None for _ in range(2 ** N)] for _ in range(N)]
travel(0, 1, N, (1 << N) - 1)

# output
sol = 123456789
for val in opt[0]:
	if val is not None: sol = min(sol, val)
print(sol)