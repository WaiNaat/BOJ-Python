import sys
input = sys.stdin.readline
print = sys.stdout.write

def DFS(pc):
	visited = [0 for _ in range(N+1)]
	stack = []
	cnt = 0

	stack.append(pc)
	while stack:
		cur = stack.pop()
		cnt += 1
		for next in company[cur]:
			if visited[next] == 0:
				stack.append(next)
	
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
	visited = [0 for _ in range(N+1)]
	connected[pc] = cnt = DFS(pc)
	if cnt > hack_max: hack_max = cnt

# output
for i in range(1, N+1): 
	if connected[i] == hack_max: print("%d " % i)