import sys
from collections import deque
input = sys.stdin.readline

# function
# v:=starting vertex, V:=number of vertices
def BFS(v, V):
	visited = [0 for _ in range(V+1)]
	q = deque([])
	cnt = 0

	visited[v] = 1
	q.append(v)

	while len(q) != 0:
		u = q.popleft()
		for adj in G[u]:
			if visited[adj] == 0:
				visited[adj] = 1
				cnt += 1
				q.append(adj)
	
	return cnt


# input
V = int(input())
E = int(input())
G = {i:set([]) for i in range(V+1)}
for _ in range(E):
	u, v = tuple(map(int, input().split()))
	G[u].add(v)
	G[v].add(u)

# process & output
print(BFS(1, V))