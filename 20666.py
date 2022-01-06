import sys
input = sys.stdin.readline
import heapq
# input
total_mob, clear_mob = map(int, input().split())
mob_hardness = list(map(int, input().split()))
tip_num = int(input())

tip = {}
for _ in range(tip_num):
	item, mob, hardness = map(int, input().split())
	item -= 1
	mob -= 1
	if item not in tip: tip[item] = set()
	tip[item].add((mob, hardness))
	mob_hardness[mob] += hardness	
# process
'''
잡고 > 정보 업데이트 > ...
난이도가 낮은 몹부터 잡으니까 최소 힙.
tip은 dict에 key를 아이템, value를 몹과 난이도의 set으로.
이미 죽은 애들은 난이도 낮추는게 소용이 없음
	>> 죽은 애들 목록 따로 만들어야 함.

h := 최소 힙. (난이도, 몹 번호)
tip := key:아이템, value:(몹 번호, 추가 난이도)
dead := 죽은 몹 번호 set
'''
h = list(zip(mob_hardness, range(total_mob)))
heapq.heapify(h)
sol = 0
dead = set()
for _ in range(clear_mob):
	# 사냥
	hunt_hardness, hunt_mob = heapq.heappop(h)
	while hunt_mob in dead: hunt_hardness, hunt_mob = heapq.heappop(h)
	sol = max(sol, hunt_hardness)
	dead.add(hunt_mob)
	# 난이도 조정
	if hunt_mob in tip:
		for mob, hardness in tip[hunt_mob]:
			if mob not in dead:
				mob_hardness[mob] -= hardness
				heapq.heappush(h, (mob_hardness[mob], mob))
# output
print(sol)