import sys
from bisect import bisect_left
input = sys.stdin.readline

# input
n = int(input())
a = set([])
bc = []

for i in range(n):
	x, y, z = tuple(map(int, (input().split())))
	a.add(x)
	bc.append((x, y, z))

# process
# sorting
a = tuple(sorted(a))
bc.sort(key=lambda x:(x[1], x[2]))

# check if A-sword can be used as BC-sword
for i in range(len(a)):
	j = bisect_left(bc, (0, a[i], 0))
	while j < len(bc) and a[i] >= bc[j][1]:
		if a[i] != bc[j][0] and a[i] <= bc[j][2]:
			bc.pop(j)
		else:
			j += 1
# now swords in bc cannot be covered by A-sword

# interval scheduling
bcCnt = 0
last = -1
for i in range(len(bc)):
	if last  < bc[i][1]:
		last = bc[i][2]
		bcCnt += 1

# output
print(len(a) + bcCnt)