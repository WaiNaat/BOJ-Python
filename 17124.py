import sys
input = sys.stdin.readline
from bisect import bisect_right

# input
T = int(input())
for _ in range(T):
	a_size, b_size = map(int, input().split())
	A = list(map(int, input().split()))
	B = list(map(int, input().split()))
# process
	'''
	B를 정렬
	A[i]에 대해
		A[i]를 B에 삽입한다면 어느 위치에 들어가야 하는지를 이분탐색으로 계산.
		A[i]가 들어갈 위치 좌우의 B 원소들이 C[i]가 될 수 있는 후보.
	'''
	B.sort()
	c_sum = 0
	for val in A:
		idx = bisect_right(B, val, 0, b_size)
		if idx == 0:
			c_sum += B[0]
		elif idx == b_size:
			c_sum += B[-1]
		else:
			if abs(B[idx - 1] - val) > abs(B[idx] - val):
				c_sum += B[idx]
			else:
				c_sum += B[idx - 1]
# output
	print(c_sum)