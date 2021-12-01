### 시간 초과 ###

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(pc, visited):
	# 이미 예전에 탐색했던 컴퓨터면 거기에 몇 개가 연결되어 있는지 알고 있음
	if connected[pc] != 0:
		visited[0] += connected[pc]
		return

	# visited[0] := 연결된 pc의 개수를 세는 데 사용
	visited[0] += 1
	visited[pc] = 1
	for next in company[pc]:
		if visited[next] == 0:
			DFS(next, visited)

# input
N, M = map(int, input().split())
company = {i:set([]) for i in range(1, N+1)}
for _ in range(M):
	a, b = map(int, input().split())
	company[b].add(a)

# process
connected = [0 for _ in range(N+1)]
for pc in company:
	visited = [0 for _ in range(N+1)]
	DFS(pc, visited)
	connected[pc] = visited[0]

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