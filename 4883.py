import sys
input = sys.stdin.readline
# input
n = int(input())
i = 0
while n != 0:
	i += 1
	G = [tuple(map(int, input().split())) for _ in range(n)]
# process
	'''
	i행 j열까지 오는 데 필요한 최소 비용을 opt(i, j)라 하면
	opt(i, j) =
		opt(i, j-1)
		opt(i-1, j-1)
		opt(i-1, j)
		opt(i-1, j+1)
		중 최솟값에 i행 j열 정점의 비용을 더한 값.
	
	cost_left/right/mid := 각각 opt(i-1, j-1), opt(i-1, j), opt(i-1, j+1)
	tmp_left/right/mid := 각각 opt(i, 0), opt(i, 1), opt(i, 2)
	'''
	cost_left = 1001
	cost_mid = G[0][1]
	cost_right = G[0][1] + G[0][2]

	for row in range(1, n):
		tmp_left = min(cost_left, cost_mid) + G[row][0]
		tmp_mid = min(cost_left, cost_mid, cost_right, tmp_left) + G[row][1]
		tmp_right = min(cost_mid, cost_right, tmp_mid) + G[row][2]
		cost_left = tmp_left
		cost_mid = tmp_mid
		cost_right = tmp_right
# output
	print(f"{i}. {cost_mid}")
	n = int(input())