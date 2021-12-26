# input
tower, bulgogi, time = map(int, input().split())
# process
'''
(타워)*x + (불고기)*y + z = 시간
max(x)=10000이므로 O(x) 완전탐색 사용 가능
'''
sol = (-1, 10001) # (햄버거, 콜라)
# 타워버거 x개 먹기
for x in range(time // tower + 1):
	t = time
	cnt = x
	t -= tower * x
	# 남은시간동안 불고기버거 최대로 먹기
	y, cola = divmod(t, bulgogi)
	cnt += y
	# 문제의 조건에 맞는지
	if cola < sol[1] or \
		(cola == sol[1] and cnt > sol[0]):
		sol = (cnt, cola)
# output
print(sol[0], sol[1])