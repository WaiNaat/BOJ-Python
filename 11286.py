import heapq
import sys
input = sys.stdin.readline
# input
h = []
n = int(input())
for _ in range(n):
	op = int(input())
# process & output
	if op == 0:
		val = heapq.heappop(h)[1] if h else 0
		print(val)
	else: heapq.heappush(h, (abs(op), op))