import sys
input = sys.stdin.readline
# input
t = int(input())
for _ in range(t):
	start, playtime = input().split()
# process
	'''
	입력에 대해서 pc방 시간을 계산하되
	야간의 경우에는 야간 정액을 끊는 경우/아닌 경우로 나눠서 생각.
	pc_time := pc방 컴퓨터 종료시간 [시간, 분]
	'''
	pc_time = list(map(int, start.split(':')))
	playtime = int(playtime)
	bill = 0
	while playtime > 0:
		# 야간에 5시간 이상 게임을 하는 경우 야간 정액 구매
		# 2200~0300 사이에 pc방 시간을 결제하는데 남은 게임 플레이 시간이 5시간 이상일 경우
		if (22 <= pc_time[0] or pc_time[0] <= 2 or (pc_time[0] == 3 and pc_time[1] == 0)) \
			 and playtime >= 300:
			# 야간에 게임하는 시간 계산
			if pc_time[0] >= 22:
				night_playtime_hr = 23 - pc_time[0]
				night_playtime_min = 60 - pc_time[1]
				if night_playtime_min == 60:
					night_playtime_min = 0
					night_playtime_hr += 1
				playtime -= 60 * night_playtime_hr + night_playtime_min + 480
			elif pc_time[0] < 8:
				night_playtime_min = 60 - pc_time[1]
				night_playtime_hr = 7 - pc_time[0]
				if night_playtime_min == 60:
					night_playtime_min = 0
					night_playtime_hr += 1
				playtime -= 60 * night_playtime_hr + night_playtime_min
			# 야간 정액권은 무조건 아침 8시에 끝남.
			bill += 5000
			pc_time = [8, 0]
		# 그게 아니면 1시간씩 결제함
		else:
			pc_time[0] = (pc_time[0] + 1) % 24
			playtime -= 60
			bill += 1000
# output
	print(bill)