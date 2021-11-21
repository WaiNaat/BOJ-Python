### 틀렸습니다 ###

import sys
from collections import deque
input = sys.stdin.readline

# input
K = int(input())
for _ in range(K):
	V, E = tuple(map(int, input().split()))
	G = {}
	for _ in range(E):
		u, v = tuple(map(int, input().split()))
		if u not in G: G[u] = set([v])
		else: G[u].add(v)
		if v not in G: G[v] = set([u])
		else: G[v].add(u)

# process
	q = deque([])
	X = set([])
	Y = set([])
	isBipartite = True

	for v in G.keys():
		if not isBipartite: continue
		vInX = True if v in X else False
		# v가 X에 있다면 v의 인접 정점은 무조건 Y에 있어야 함.
		if vInX:
			for adj in G[v]:
				if adj in X:
					isBipartite = False
					break
				Y.add(adj)
		# v가 X에 없다면 v는 Y에 있어야 하고,
		# v의 인접 정점은 무조건 X에 있어야 함.
		else:
			Y.add(v)
			for adj in G[v]:
				if adj in Y:
					isBipartite = False
					break
				X.add(adj)

# output
	if isBipartite: print("YES")
	else: print("NO")