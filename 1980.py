# input
tower, bulgogi, time = map(int, input().split())
# process
'''
(타워)*x + (불고기)*y + z = 시간
max(x)=max(z)=10000 이므로 O(xz) 완전탐색 사용 가능?
'''
sol = (-1, 10001) # (햄버거, 콜라)
for cola in range(time):
	# 콜라를 일단 cola 시간만큼 마시기 <<< 이럴 필요가 있나?
	t_init = time - cola
	for x in range(t_init // tower + 1):
		t = t_init
		# 타워버거 x개 먹기
		cnt = x
		t -= tower * x
		# 남은시간동안 불고기버거 최대로 먹기
		y, bonus_cola = divmod(t, bulgogi)
		cnt += y
		# 정답인지 판단
		if cola + bonus_cola < sol[1] or \
			(cola + bonus_cola == sol[1] and cnt > sol[0]):
			sol = (cnt, cola + bonus_cola)
	# 만약 sol 구해진 게 있으면 종료(문제 조건 1)
	if sol[0] != -1: break
# output
print(sol[0], sol[1])