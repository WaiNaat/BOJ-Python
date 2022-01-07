import sys
input = sys.stdin.readline
import heapq as hq
# input
t = int(input())
for _ in range(t):
	chapter = int(input())
	pages = list(map(int, input().split()))
# process
	'''
	각 장이 섞여도 됨.
	>> 힙에서 제일 작은 거 두 개 합치고 다시 넣음.
	'''
	sol = 0
	hq.heapify(pages)
	for _ in range(chapter - 1):
		cost = hq.heappop(pages) + hq.heappop(pages)
		sol += cost
		hq.heappush(pages, cost)
# output
	print(sol)