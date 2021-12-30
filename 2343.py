# function
def record(size):
	'''
	size 크기의 블루레이로 강의들을 녹화했을 때
	필요한 블루레이의 수를 반환.
	'''
	cnt = 1
	cur = 0
	for lecture in lectures:
		# 이 크기로는 절대 녹화 못하는 경우
		if lecture > size: return 100001
		# 녹화했을 때 넘어가면 블루레이 교체
		if lecture + cur > size:
			cnt += 1
			cur = 0
		cur += lecture
	return cnt

# input
lecture_num, blueray_num = map(int, input().split())
lectures = tuple(map(int, input().split()))
# process
'''
블루레이의 크기를 x,
x크기로 강의를 담았을 때 y개의 블루레이에 담긴다고 한다면
y > 목표치: x를 늘려야 함.
y <= 목표치: x를 줄여야 함.
'''
left = 0
right = sum(lectures) + 1
while left < right:
	mid = (left + right) // 2
	if record(mid) > blueray_num:
		left = mid + 1
	else: 
		right = mid
# output
print(left)