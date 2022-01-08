import sys
input = sys.stdin.readline
# input
n, k = map(int, input().split())
point = [int(input()) for _ in range(n)]
# process
'''
어떤 사이클이 나올 때까지 돌린다.
사이클 안에 보성이가 있는지 없는지 확인한다.

pointed_people := 지목당한 사람들 집합.
cur := 현재 지목당한 사람.
'''
pointed_people = set([0])
cur = cnt = 0
found = False
while True:
	cnt += 1
	cur = point[cur]
	# 보성이 당첨
	if cur == k:
		found = True
		break
	# 사이클이 완성되었을 경우
	elif cur in pointed_people:
		break
	else:
		pointed_people.add(cur)
# output
print(cnt if found else -1)