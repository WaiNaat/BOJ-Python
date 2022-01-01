# functions
def blow(time):
	cnt = 0
	for s in staff: cnt +=  time // s
	return cnt

# input
n, m = map(int, input().split())
staff = tuple(map(int, input().split()))
# process
'''
시간 최소 >> bisect_left의 원리
x분 동안 k개의 풍선을 만든다고 할 때
k >= M: x를 줄여야 함.
k < M: x를 늘려야 함.

right := 가장 빨리 부는 사람이 혼자 다 불 때 걸리는 시간
'''
left = 1
right = min(staff) * m + 1
while left < right:
	mid = (left + right) // 2
	if blow(mid) >= m: right = mid
	else: left = mid + 1
# output
print(left)