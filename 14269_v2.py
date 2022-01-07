### 틀렸습니다 ###

import sys
input = sys.stdin.readline

# input
n = int(input())
a = set([])
bc_all = []

for i in range(n):
	x, y, z = tuple(map(int, (input().split())))
	a.add(x)
	bc_all.append((x, y, z))

# process
# sorting
a = tuple(sorted(a))
bc_all.sort(key=lambda x:(x[2], -x[1]))

# interval scheduling
bc = []
last = 0
for i in range(n):
	if bc_all[i][1] > last:
		last = bc_all[i][2]
		bc.append(bc_all[i])

# check if right-hand sword can be used as left-hand sword
aIdx = 0
bcIdx = 0
bcCnt = len(bc)
while aIdx < len(a) and bcIdx < len(bc):
	if bc[bcIdx][1] <= a[aIdx] <= bc[bcIdx][2]:
		if a[aIdx] != bc[bcIdx][0]:
			bcCnt -= 1
			bcIdx += 1
			aIdx += 1
		else:
			aIdx += 1
	elif a[aIdx] < bc[bcIdx][1]:
		aIdx += 1
	elif a[aIdx] > bc[bcIdx][2]:
		bcIdx += 1

# output
print(len(a) + bcCnt)