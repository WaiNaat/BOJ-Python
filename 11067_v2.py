import sys
input = sys.stdin.readline
# input
T = int(input())
for _ in range(T):
	n = int(input())
	cafe = {}
	for _ in range(n):
		x, y = map(int, input().split())
		if x not in cafe: cafe[x] = []
		cafe[x].append(y)
	m = tuple(map(int, input().split()))[1:]
# process
	'''
	x=i 에서 마지막 카페의 y좌표를 j라 할 때
	x=i+1 에서 처음 카페의 y좌표는 j이다.

	x=i 에서 처음 카페의 y좌표를 j라 할 때
	max(x=i에서 y좌표들)=j 면 아래로 내려가는 경로
	아니면 위로 올라가는 경로.
	'''
	x = 0
	y = 0
	cafeNo = 0
	cafeList = {i:None for i in m}
	while cafeNo < n:
		while x not in cafe: x += 1
		cafe[x].sort()
		if cafe[x][-1] == y: cafe[x].reverse()
		for j in cafe[x]:
			y = j
			cafeNo += 1
			if cafeNo in cafeList:
				cafeList[cafeNo] = (x, y)
		x += 1
# output
	for i in m: print(*cafeList[i])