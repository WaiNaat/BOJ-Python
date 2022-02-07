import sys
input = sys.stdin.readline
from collections import deque
# input
n = int(input())
G = [[] for _ in range(n + 1)]
for _ in range(n - 1):
	i, j = map(int, input().split())
	G[i].append(j)
	G[j].append(i)
# process
'''
BFS로 1부터 탐색하면서 들어가면
자동적으로 해당 노드의 자식들을 한 번에 탐색한다.
큐에 본인과 연결된 정점을 집어넣을 때 부모 번호를 저장.
'''
parent = [None for _ in range(n + 1)]

q = deque([1])
while q:
	cur = q.popleft()
	for next in G[cur]:
		if parent[next] is None:
			parent[next] = cur
			q.append(next)
# output
print(*parent[2:], sep='\n')