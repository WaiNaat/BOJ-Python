import sys
input = sys.stdin.readline
# input
T = int(input())
for _ in range(T):
	cars, track, boost_limit = map(int, input().split())
	v = list(map(int, input().split()))
# process & output
	'''
	일단 내 속도와 나머지들의 최고 속도를 비교
		부스터 안 쓰고도 단독우승 되는지 판단가능.
	부스터를 쓸 경우 필요한 최소 이동거리 계산
		라이벌이 t초면 트랙을 완주한다고 했을 때
		나는 t-1초동안 움직이고 남은 거리만큼 부스터를 써야 공동 1등임.
	'''
	my_speed = v.pop()
	rival_speed = max(v)
	if my_speed > rival_speed: print(0)
	else:
		rival_time = track / rival_speed
		my_booster = int(track - (rival_time - 1) * my_speed + 1)
		if my_booster > boost_limit: print(-1)
		else: print(my_booster)