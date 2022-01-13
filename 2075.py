### 메모리 초과 ###

import sys, heapq
input = sys.stdin.readline
# input
n = int(input())
line = [[] for _ in range(n)]
for _ in range(n):
	nums = tuple(map(int, input().split()))
	for i in range(n):
		line[i].append(nums[i])
# process
'''
각 세로줄을 저장하는 배열 n개.
각 세로줄에서 가장 큰 수를 모은 최대 힙 1개.

1. 각 세로줄에서 가장 큰 수를 빼서 최대 힙에 넣는다.
2. 힙에서 가장 큰 수를 뺀다.
3. 해당 숫자가 몇 번째 세로줄에서 왔는지 보고,
4. 그 줄에서 가장 큰 수를 빼서 다시 힙에 넣는다.
5. 2번부터 다시 반복.
'''
h = []
for i in range(n):
	val = line[i].pop()
	h.append((-val, i))
heapq.heapify(h)

cnt = sol = 0
while cnt < n:
	cnt += 1
	sol, i = heapq.heappop(h)
	if line[i]:
		heapq.heappush(h, (-line[i].pop(), i))
# output
print(-sol)