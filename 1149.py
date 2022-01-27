# input
n = int(input())
rTotalCost = [None for _ in range(n)]
gTotalCost = [None for _ in range(n)]
bTotalCost = [None for _ in range(n)]
rTotalCost[0], gTotalCost[0], bTotalCost[0] = map(int, input().split())
for i in range(1, n):
	rCost, gCost, bCost = map(int, input().split())
# process
	'''
	i번째 집을 빨강, 초록, 파랑으로 칠하는 비용을 각각
	rCost(i), gCost(i), bCost(i)라 하고
	그렇게 칠했을 때의 총 비용을 rTotalCost(i), gTotalCost(i), bTotalCost(i)라 하면
	rTotalCost(i) = min(gTotalCost(i-1), bTotalCost(i-1)) + rCost(i)
	같은 방식으로 gTotalCost(i)와 bTotalCost(i)도 구할 수 있음.
	'''
	rTotalCost[i] = min(gTotalCost[i - 1], bTotalCost[i - 1]) + rCost
	gTotalCost[i] = min(rTotalCost[i - 1], bTotalCost[i - 1]) + gCost
	bTotalCost[i] = min(rTotalCost[i - 1], gTotalCost[i - 1]) + bCost
# output
n -= 1
print(min(rTotalCost[n], gTotalCost[n], bTotalCost[n]))