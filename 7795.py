import sys
input = sys.stdin.readline
# input
t = int(input())
for _ in range(t):
	aLen, bLen = map(int, input().split())
	A = tuple(map(int, input().split()))
	B = list(map(int, input().split()))
# process
	'''
	B를 정렬.
	a in A에 대해 이분탐색으로 구할 수 있음.
	작은 먹이만 먹을 수 있다: bisect_left의 원리
	a <= b: 왼쪽으로
	a > b: 오른쪽으로
	'''
	B.sort()
	cnt = 0
	for a in A:
		left = 0
		right = bLen
		while left < right:
			mid = (left + right) // 2
			if a <= B[mid]: right = mid
			else: left = mid + 1
		cnt += left
# output
	print(cnt)