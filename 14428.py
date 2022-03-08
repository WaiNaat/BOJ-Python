### 시간 초과 ###


import sys
input = sys.stdin.readline

# 수열 입력
n = int(input())
A = list(map(int, input().split()))

# 쿼리 입력
m = int(input())
for _ in range(m):
	q, a, b = map(int, input().split())

	# 1번 쿼리
	if q == 1:
		A[a - 1] = b
	
	# 2번 쿼리
	else:
		minIdx = 0
		minVal = 1234567890
		for i in range(a - 1, b):
			if A[i] < minVal:
				minVal = A[i]
				minIdx = i
		print(minIdx + 1)