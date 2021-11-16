import sys
input = sys.stdin.readline

# function
def DFS(v, visited):
	visited[v] = 1
	global cnt
	cnt += 1

	for adj in G[v]:
		if visited[adj] == 0:
			DFS(adj, visited)


# input
V = int(input())
E = int(input())
G = {i:set([]) for i in range(V+1)}
for _ in range(E):
	u, v = tuple(map(int, input().split()))
	G[u].add(v)
	G[v].add(u)

# process
cnt = 0
DFS(1, [0 for _ in range(V+1)])

# output
print(cnt-1)