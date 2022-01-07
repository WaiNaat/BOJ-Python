import sys
input = sys.stdin.readline
# input
n = int(input())
extentions = {}
for _ in range(n):
	file = input().rstrip()
# process
	'''
	확장자 구하고 dict로 정리.
	'''
	_, _, ext = file.partition('.')
	if ext not in extentions: extentions[ext] = 0
	extentions[ext] += 1
names = list(extentions.keys())
names.sort()
# output
for name in names: print(f"{name} {extentions[name]}")