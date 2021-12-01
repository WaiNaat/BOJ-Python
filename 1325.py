### 시간 초과 ###
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(pc, visited):
	# visited[0] contains number of connected computers
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
hackList = []
for pc in company:
	visited = [0 for _ in range(N+1)]
	DFS(pc, visited)
	hackList.append((visited[0], pc))
hackList = sorted(hackList, key = lambda x: (-x[0], x[1]))
# output
hack_max = hackList[0][0]
hackCnt = hack_max
i = 0
while hackCnt == hack_max:
	print(hackList[i][1], end=' ')
	i += 1
	hackCnt = hackList[i][0]