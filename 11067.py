### 시간 초과 ###
'''
그리고 모든 코너에는 카페가 들어서 있다
그리고 모든 코너에는 카페가 들어서 있다
그리고 모든 코너에는 카페가 들어서 있다
그리고 모든 코너에는 카페가 들어서 있다
그리고 모든 코너에는 카페가 들어서 있다
그리고 모든 코너에는 카페가 들어서 있다
그리고 모든 코너에는 카페가 들어서 있다
그리고 모든 코너에는 카페가 들어서 있다
그리고 모든 코너에는 카페가 들어서 있다
'''

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
	x=0에서의 이동방향을 정한다.
	x=i에서 이동이 아래방향이면 x=i+1에서는 위 방향.
	반대면 반대.

	카페는 dictionary 형태로 x좌표를 key로, y좌표들의 list를 value로 갖는다.
	'''
	isUpDown = True if max(cafe[0]) == 0 else False
	x = 0
	cafeList = [-1]
	isEnd = False
	while x <= max(cafe.keys()):
		if x not in cafe:
			x += 1
			continue
		# 카페 정렬
		cafe[x].sort(reverse=True) if isUpDown else cafe[x].sort()
		# 번호 붙이기
		for y in cafe[x]: cafeList.append((x, y))
		x += 1
		isUpDown = not isUpDown
# output
	for i in m: print(cafeList[i][0], cafeList[i][1])