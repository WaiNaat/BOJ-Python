import sys
input = sys.stdin.readline
# function
def check_in(time):
	'''
	time 시간 동안 심사받을 수 있는 최대 인원 반환.
	'''
	cnt = 0
	for d in desk: cnt += time // d
	return cnt

# input
n, m = map(int, input().split())
desk = [int(input()) for _ in range(n)]
# process
'''
t분 동안 모든 심사관들이 검사하는 사람 수 k
k < m: t를 늘려야 함.
k >= m: t를 줄여야 함.
k명 검사하는데 드는 시간 중 최소: bisect_left의 원리

t 최소는 1, 최대는 가장 빠른 검사관이 혼자 다 할 때.
'''
left = 1
right = min(desk) * m + 1
while left < right:
	mid = (left + right) // 2
	if check_in(mid) < m: left = mid + 1
	else: right = mid
# output
print(left)