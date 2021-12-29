### 틀렸습니다 ###

import sys
input = sys.stdin.readline
from bisect import bisect_right
# input
n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
# process
'''
빈집없을때 이론상 최대 거리=(오른쪽집-왼쪽집)/(공유기-1)
빈집이 있으면? 이론상 최대 거리에 가장 가까운 녀석으로 고른다.

가장 왼쪽 집에 공유기를 설치한다.
공유기가 설치된 집 중 가장 오른쪽 집을 고른다.
	그 집 오른쪽 집들 중 이론상~집에 공유기를 설치한다.
'''
house.sort()
d = (house[-1] - house[0]) // (c - 1)
c -= 1
cur = house[0]
left = 1
right = len(house)
sol = None

while c > 0:
	idx = bisect_right(house, cur + d, lo=left, hi=right)
	tmp1 = abs(d - (house[idx] - cur))
	tmp2 = abs(d - (house[idx - 1] - cur))
	prev = cur
	if tmp1 > tmp2:
		left = idx
		cur = house[idx - 1]
	else:
		left = idx + 1
		cur = house[idx]
	c -= 1
	if sol is None: sol = cur - prev
	elif sol > cur - prev: sol = cur - prev
# output
print(sol)