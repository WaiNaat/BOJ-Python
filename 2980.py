import sys
input = sys.stdin.readline
# input
N, L = map(int, input().split())
road = [None for _ in range(L + 1)]
for _ in range(N):
	d, r, g = map(int, input().split())
	road[d] = (r, g)
# process
'''
max(N)=max(R)=100, max(L)=1000이므로 
상근이의 최대 대기시간은 10000초 + 이동시간은 1000초.
'''
cur = 1
time = 0
while cur < L:
	# 지금 위치에 신호등이 없을 경우 움직임
	if road[cur] is None: cur += 1
	# 신호등이 있으면
	else:
		r, g = road[cur]
		# 초록불일 경우 움직임
		if not 0 <= time % (r + g) < r: cur += 1
	time += 1	
# output
print(time)