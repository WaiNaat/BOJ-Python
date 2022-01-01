import sys
input = sys.stdin.readline
import math
# input
t = int(input())
for _ in range(t):
	n, k = map(int, input().split())
# process
	'''
	등차수열의 합: 뛴 거리 계산
	i번째 전환점 도달:
		홀수면 왼쪽, 짝수면 오른쪽 보고 있음.

	i를 이분탐색 없이 구하는 법?
	뛴 거리 = n-1 이 되는 i를 구하는 법
		>> 이차방정식?
		(i * (i + 1) * k) // 2 = n - 1
	'''
	i = int((-1 + math.sqrt(1 + 4 * ((n - 1) * 2 / k))) / 2)

	direction = None
	pos = None
	distance = (i * (i + 1) * k) // 2
	if i % 2 == 1:
		direction = 'L'
		pos = (i // 2 + 1) * k - (n - 1 - distance)
	else:
		direction = 'R'
		pos = -(i // 2) * k + (n - 1 - distance)
# output
	print(pos, direction)