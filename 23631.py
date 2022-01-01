import sys
input = sys.stdin.readline
# input
t = int(input())
for _ in range(t):
	n, k = map(int, input().split())
# process
	'''
	등차수열의 합: 뛴 거리 계산
	i번째 전환점 도달:
		홀수면 왼쪽, 짝수면 오른쪽 보고 있음.

	등차수열의 합이 n보다 작은 i값 찾기
	합 > n-1: i를 줄인다.
	합 <= n-1: i를 늘린다.

	n보다 작은 i중 최대: bisect_right의 원리
	'''
	run = lambda i: (i * (i + 1) * k) // 2
	left = 0
	right = n # i=n-1이면 확실하게 합>n-1임.
	while left < right:
		mid = (left + right) // 2
		if run(mid) > n - 1: right = mid
		else: left = mid + 1
	
	i = left - 1
	direction = None
	pos = None
	distance = run(i)
	if i % 2 == 1:
		direction = 'L'
		pos = (i // 2 + 1) * k - (n - 1 - distance)
	else:
		direction = 'R'
		pos = -(i // 2) * k + (n - 1 - distance)
# output
	print(pos, direction)