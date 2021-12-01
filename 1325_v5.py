import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

def BFS(pc):
	visited = [0 for _ in range(N+1)]
	q = deque([])
	
	cnt = 1
	visited[pc] = 1
	q.append(pc)
	while q:
		cur = q.popleft()
		for next in company[cur]:
			if visited[next] == 0:
				visited[next] = 1
				cnt += 1
				q.append(next)
	return cnt

# input
N, M = map(int, input().split())
company = {i:set([]) for i in range(1, N+1)}
for _ in range(M):
	a, b = map(int, input().split())
	company[b].add(a)

# process
connected = [0 for _ in range(N+1)]
hack_max = 0
for pc in company:
	connected[pc] = cnt = BFS(pc)
	if cnt > hack_max: hack_max = cnt

# output
for i in range(1, N+1): 
	if connected[i] == hack_max: print("%d " % i)