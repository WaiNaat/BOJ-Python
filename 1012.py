import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# functions
def worm():
	visited = {v:0 for v in G.keys()}
	cnt = 0
	for v in visited:
		if visited[v] == 0:
			cnt += 1
			DFS(v, visited)
	return cnt

def DFS(v, visited):
	visited[v] = 1
	for adj in G[v]:
		if visited[adj] == 0:
			DFS(adj, visited)

	
# input
T = int(input())
for _ in range(T):
	M, N, K = tuple(map(int, input().split()))
	G = {}
	for _ in range(K):
		v = tuple(map(int, input().split()))
		v = v[0] * 100 + v[1]
		if v not in G: G[v] = set([])
		# up
		if v-1 in G:
			G[v].add(v-1)
			G[v-1].add(v)
		# down
		if v+1 in G:
			G[v].add(v+1)
			G[v+1].add(v)
		# left
		if v-100 in G:
			G[v].add(v-100)
			G[v-100].add(v)
		# right
		if v+100 in G:
			G[v].add(v+100)
			G[v+100].add(v)

# process & output
	print(worm())