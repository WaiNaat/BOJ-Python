import sys
input = sys.stdin.readline
import heapq as hq
# input & process
'''
고릴라 목록을 dict로 만든다.
	key:이름, value:정보들 최대 힙.
'''
q = int(input())
gorilla = {}
value = 0
for _ in range(q):
	info = input().split()
	name = info[1]
	# 고릴라 정보
	if info[0] == '1':
		if name not in gorilla: gorilla[name] = []
		for c in info[3:]: hq.heappush(gorilla[name], -int(c))
	# 정보 거래
	else:
		for _ in range(int(info[2])):
			if name not in gorilla or not gorilla[name]: break
			value -= hq.heappop(gorilla[name])
# output
print(value)