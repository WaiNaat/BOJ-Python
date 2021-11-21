import sys
from collections import deque
input = sys.stdin.readline

# functions
# 최종 결과: visited의 값으로 그래프 분할 가능: -1인 애들과 +1인 애들
def bipartite(V):
	visited = [0 for _ in range(V+1)]
	sol = True
	for i in range(1, V+1):
		if visited[i] == 0:
			sol = BFS(visited, i)
		if not sol: break
	return sol

def BFS(visited, i):
	q = deque([])
	isBipartite = True

	visited[i] = 1
	q.append(i)

	while q and isBipartite:
		v = q.popleft()
		group = visited[v]

		for adj in G[v]:
			# 아직 탐색되지 않은 애들이면 현재 정점과 반대되는 집합에 넣어줌
			if visited[adj] == 0:
				visited[adj] = -group
				q.append(adj)
			# 현재 정점에 인접한 녀석이 현재 정점과 같은 집합이면 이분 그래프가 아님
			elif visited[adj] == group:
				isBipartite = False
				break
	return isBipartite


# input
K = int(input())
for _ in range(K):
	V, E = tuple(map(int, input().split()))
	G = {i:set([]) for i in range(V+1)}
	for _ in range(E):
		u, v = tuple(map(int, input().split()))
		G[v].add(u)
		G[u].add(v)

# process & output
	if bipartite(V): print("YES")
	else: print("NO")