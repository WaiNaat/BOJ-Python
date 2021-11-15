import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

# functions
def DFS(v, visited):
	visited[v] = 1
	print("%d " % v)

	for adjv in sorted(G[v]):
		if visited[adjv] == 0:
			DFS(adjv, visited)

def BFS(v, n):
	visited = [0 for _ in range(N+1)]
	q = deque([])

	visited[v] = 1
	print("%d " % v)
	q.append(v)

	while len(q) != 0:
		u = q.popleft()
		for adjv in sorted(G[u]):
			if visited[adjv] == 0:
				visited[adjv] = 1
				print("%d " % adjv)
				q.append(adjv)

# input
N, M, V = tuple(map(int, input().split()))
G = {i:set([]) for i in range(N+1)}
for _ in range(M):
	u, v = tuple(map(int, input().split()))
	G[u].add(v)
	G[v].add(u)

# process & output
DFS(V, [0 for _ in range(N+1)])
print("\n")
BFS(V, N)