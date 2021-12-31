import sys
input = sys.stdin.readline
# functions
def trim(gimbap):
	'''
	김밥 한 줄에 대해 꼬다리 손질해주는 함수.
	'''
	global k
	# 일단 양쪽 꼬다리 자름
	gimbap -= k * 2
	# 한쪽만 k만큼 자르면 되는 경우 한쪽 꼬다리 복구
	if gimbap < 0: gimbap += k
	return gimbap if gimbap > 0 else 0

def cut(length):
	'''
	length 길이로 김밥을 잘랐을 때 나오는 김밥 수 반환.
	'''
	cnt = 0
	for gimbap in trimmed_gimbaps: cnt += gimbap // length
	return cnt
	
# input
n, k, m = map(int, input().split())
gimbaps = [int(input()) for _ in range(n)]
# process
'''
일단 손질했으면 한쪽만 꼬다리가 살아있어도 됨.

P를 최대로 >> bisect_right의 원리.

일단 꼬다리 손질.
P길이로 자른 조각의 개수 i가
i >= M: P를 늘려야 함.
i < M: P를 줄여야 함.
'''
# 손질
trimmed_gimbaps = []
gb_sum = 0
for gb in gimbaps:
	trimmed = trim(gb)
	if trimmed > 0:
		trimmed_gimbaps.append(trimmed)
		gb_sum += trimmed
# p가 없을 경우: m이 너무 많거나 김밥이 없는 경우
sol = -1
if trimmed_gimbaps and gb_sum >= m:
	left = 1
	right = max(trimmed_gimbaps) + 1
	while left < right:
		mid = (left + right) // 2
		if cut(mid) >= m: left = mid + 1
		else: right = mid
	sol = left - 1
# output
print(sol)