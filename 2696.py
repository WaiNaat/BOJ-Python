import sys
input = sys.stdin.readline
import heapq
# input
t = int(input())
for _ in range(t):
	m = int(input())
	seq = []
	for _ in range(m, 0, -10):
		seq.append(map(int, input().split()))
# process
	'''
	왼쪽 힙: 최대 힙, 중앙값 이하의 값들.
	오른쪽 힙: 최소 힙, 중앙값 이상의 값들.
	조건: 항상 왼쪽 힙의 크기가 오른쪽 힙과 같거나 1 더 크게.
	왼쪽 힙의 root가 중앙값.
	'''
	left = []
	right = []
	sol = []
	isOdd = True
	for mini_seq in seq:
		for val in mini_seq:
			# 숫자 입력
			if not left or -left[0] >= val:
				heapq.heappush(left, -val)
			else:
				heapq.heappush(right, val)
			# 조건에 맞게 힙 크기 조정
			if len(left) < len(right):
				heapq.heappush(left, -heapq.heappop(right))
			elif len(left) > len(right) + 1:
				heapq.heappush(right, -heapq.heappop(left))
			# 홀수번째 수면 중앙값 저장
			if isOdd: sol.append(-left[0])
			isOdd = not isOdd
# output
	print(len(sol))
	print_cnt = 0
	for i in range(0, len(sol)):
		if print_cnt == 0 and i > 0: print()
		print(sol[i], end=' ')
		print_cnt += 1
		print_cnt %= 10
	print()