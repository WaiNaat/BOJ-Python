import heapq
import sys
input = sys.stdin.readline
# input
n = int(input())
h = []
for _ in range(n):
	op = int(input())
# process & output
	if op == 0: print(-heapq.heappop(h) if h else 0)
	else: heapq.heappush(h, -op)