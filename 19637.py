'''
이분탐색
'''
import sys
input = sys.stdin.readline

# input
N, M = map(int, input().split())
title = tuple(map(
	lambda x: (x[0], int(x[1])), [input().split() for _ in range(N)]
))

# process
sol = []
for _ in range(M):
	power = int(input())

	left = 0
	right = N
	while left < right:
		mid = (left + right) // 2

		if title[mid][1] < power:
			left = mid + 1
		else:
			right = mid
			
	sol.append(title[left][0])

# output
print('\n'.join(sol))