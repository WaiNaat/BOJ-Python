import sys
input = sys.stdin.readline
from math import ceil
# input
n, atk = map(int, input().split())
max_hp = 0
cur_hp = 0
for _ in range(n):
	t, a, h = map(int, input().split())
# process
	'''
	방 순서대로 진행하면서 용사의 체력이 모자라면 그만큼 올린다.
	'''
	if t == 1:
		dmg = a * (ceil(h / atk) - 1) # 용사가 선공이라 한 대 덜 맞음
		cur_hp -= dmg
		# 몹을 잡고 용사의 피가 0 이하면 훈련으로 체력을 늘려야 함.
		# 최소한의 체력으로 이겨야 하니까 현재 체력은 1로 유지해야 함.
		if cur_hp <= 0:
			max_hp += -cur_hp + 1
			cur_hp = 1
	else:
		atk += a
		cur_hp = min(max_hp, cur_hp + h)
# output
print(max_hp)