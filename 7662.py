import sys
input = sys.stdin.readline
import heapq
# input & process
'''
최대 힙과 최소 힙을 만들어서
최댓값 뺄 때는 최대 힙에서,
최솟값 뺄 때는 최소 힙에서.
Q에 들어있는 원소들의 개수는 dict로.
'''
t = int(input())
for _ in range(t):
	q = {}
	max_heap = []
	min_heap = []
	k = int(input())
	# 연산 실행
	for _ in range(k):
		op, val = input().split()
		val = int(val)
		if op == 'I':
			if val not in q: q[val] = 0
			q[val] += 1
			heapq.heappush(max_heap, -val)
			heapq.heappush(min_heap, val)
		else:
			if not q: continue
			if val == 1:
				del_val = -heapq.heappop(max_heap)
				# 만약 이미 삭제된 값인데 최대 힙에 들어있던 거라면 다음 값 가져옴.
				while del_val not in q: del_val = -heapq.heappop(max_heap)
			else:
				del_val = heapq.heappop(min_heap)
				while del_val not in q: del_val = heapq.heappop(min_heap)
			q[del_val] -= 1
			if q[del_val] == 0: q.pop(del_val)
# output
	if q: print(max(q.keys()), min(q.keys()))
	else: print("EMPTY")