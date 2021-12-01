### 틀렸습니다 ###
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(pc, visited, visiting):
	visited[pc] = 1
	for i in visiting:
		connected[i] += 1
	
	for next in company[pc]:
		if visited[next] == 0:
			visiting.append(next)
			DFS(next, visited, visiting)
			visiting.pop()
		else: # 이미 방문한 pc는 자기가 몇 개와 연결되었는지 알고 있음
			connected[pc] += connected[next]


# input
N, M = map(int, input().split())
company = {i:set([]) for i in range(1, N+1)}
for _ in range(M):
	a, b = map(int, input().split())
	company[b].add(a)

# process
connected = [0 for _ in range(N+1)] # 각 pc를 해킹하면 해킹되는 컴퓨터 수
visited = [0 for _ in range(N+1)]
for pc in company:
	if visited[pc] == 0:
		visiting = [pc] # 현재 pc에 연결되어 있는 pc 목록
		DFS(pc, visited, visiting)

hack_max = connected[1]
hack_list = []
for i in range(1, N+1):
	val = connected[i]
	if val == hack_max:
		hack_list.append(i)
	elif val > hack_max:
		hack_list = [i]
		hack_max = val

# output
for x in hack_list: print(x, end=' ')