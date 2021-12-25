### 시간 초과 ###

import sys
input = sys.stdin.readline
# input
max_y, max_x, block_init = map(int, input().split())
land = [tuple(map(int, input().split())) for _ in range(max_y)]
# process
'''
max(N)=max(M)=500이고 땅의 높이를 k라 할 때 max(k)=256이므로
O(kMN) 완전탐색 알고리즘 사용 가능.

>> elementary operation 횟수가 loop당 최소 5회라서 안되는듯?
'''
sol = (-1, -1) # (time, height)
for height in range(257):
	inventory = block_init
	time = 0
	# 지면을 height의 높이로 평탄화
	for y in range(max_y):
		for x in range(max_x):
			block_needed = height - land[y][x]
			if block_needed < 0: # 지면을 깎아야 함
				time += -block_needed * 2
			else: # 지면에 블록을 쌓아야 함
				time += block_needed
			inventory -= block_needed
	if inventory < 0: continue # 평탄화 불가
	if sol[0] >= time or sol[0] == -1:
		sol = (time, height)
# output
print(sol[0], sol[1])