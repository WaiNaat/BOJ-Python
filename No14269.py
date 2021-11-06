### 시간 초과 ###

import sys
input = sys.stdin.readline

# input
n = int(input())
a = set([])
bc = []

for i in range(n):
	x, y, z = tuple(map(int, (input().split())))
	a.add(x)
	bc.append([(x, y, z), 1])

# process
for swordA in a:
	for i in range(n):
		x, y, z = bc[i][0]
		# swordA==x면 단일검을 한쪽 손에 들어야 해서 그걸로 범위검 커버를 칠 수 없다
		if y <= swordA <= z and swordA != x:
			bc[i][1] -= 1
			
# 이제 정렬하고 회의실 배정하면 됨
bc_new = []
for i in range(n):
	if bc[i][1] == 1:
		bc_new.append((bc[i][0][1], bc[i][0][2]))

bc_new.sort(key=lambda x:(x[1], x[0]))

bc_cnt = 1
last = bc_new[0][1]
for i in range(1, len(bc_new)):
	if bc_new[i][0] > last:
		last = bc_new[i][1]
		bc_cnt += 1

# output
print(len(a) + bc_cnt)