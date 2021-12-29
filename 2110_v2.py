import sys
input = sys.stdin.readline
# function
def install(dist):
	'''
	집들에 공유기를 설치하고 그 개수를 반환.
	1. 공유기 사이의 거리가 최소 dist가 되도록 설치.
	2. 최대한 촘촘하게 설치.
	'''
	cnt = 1
	cur = house[0]
	for h in house:
		if cur + dist <= h:
			cur = h
			cnt += 1
	return cnt

# input
n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
# process
'''
d := 가장 인접한 두 공유기 사이의 거리
어떤 d에 대해서 
k := d를 만족하도록 공유기를 설치했을 때 설치된 공유기 수
c > k 면 d를 줄여야 함.
c <= k 면 d를 늘려야 함.
'''
house.sort()
left = 1
right = house[-1] + 1
while left < right:
	mid = (left + right) // 2
	if install(mid) < c: right = mid
	else: left = mid + 1
# output
print(left - 1)