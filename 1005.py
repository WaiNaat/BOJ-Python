'''
topological sort
어떤 건물의 완공시간을 기록하는 배열 추가로 필요
'''
import sys
from collections import deque
input = sys.stdin.readline

def solve():
	# input
	N, K = map(int, input().split())
	D = tuple(map(int, input().split()))

	E = [[] for _ in range(N)]
	parents = [0 for _ in range(N)]

	for _ in range(K):
		prev, next = map(lambda x: int(x) - 1, input().split())
		E[prev].append(next)
		parents[next] += 1

	W = int(input()) - 1

	# process
	q = deque()
	for i in range(N):
		if parents[i] == 0:
			q.append(i)

	end_time = [0 for _ in range(N)]

	while q:
		cur = q.popleft()
		end_time[cur] += D[cur]

		if cur == W:
			return end_time[W]

		for next in E[cur]:
			parents[next] -= 1
			end_time[next] = max(end_time[cur], end_time[next])

			if parents[next] == 0:
				q.append(next)


T = int(input())
sol = []
for _ in range(T):
	sol.append(str(solve()))
print('\n'.join(sol))