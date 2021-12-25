import sys
input = sys.stdin.readline
# input
y, x, block_init = map(int, input().split())
land = [0 for _ in range(257)]
for _ in range(y):
	for height in map(int, input().split()):
		land[height] += 1
# process
'''
0~256 높이의 지형이 몇 개씩 있는지 계산. (입력 받으면서 계산함)
높이를 k라 했을 때 max(k)=256이므로 O(k^2) 완전탐색 알고리즘 사용 가능.
'''
sol = (-1, -1) # (time, height)
for flat_height in range(256, -1, -1):
	time = 0
	inven = block_init
	for land_height in range(257):
		block_needed = land[land_height] * (flat_height - land_height)
		if block_needed < 0: # 땅을 깎아야 함
			time += -block_needed * 2
		else: # 땅에 블록을 쌓아야 함
			time += block_needed
		inven -= block_needed
	if inven < 0: continue
	if sol[0] > time or sol[0] == -1:
		sol = (time, flat_height)
# output
print(sol[0], sol[1])