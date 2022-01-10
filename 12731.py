import sys, heapq
input = sys.stdin.readline
# function: 시계 덧셈용 함수.
addTime = lambda time, min: (time[0]+1, time[1]+min-60) if time[1]+min >= 60 else (time[0], time[1]+min)
# input & process
'''
기차 출발시간별로 정렬.
A역 기차 도착시간 최소 힙,
B역 기차 도착시간 최소 힙.
기차를 순서대로 출발시키는데
	각 역에 이미 도착한 기차가 있을 경우
		그 기차를 출발시키면 됨
	아니면 새로운 기차 출발.
	반대쪽 역 힙에 도착시간+회차시간 push
'''
n = int(input())
for case in range(1, n + 1):
	t = int(input())
	na, nb = map(int, input().split())
	# 기차 출발시간별로 정렬
	trains = []
	for _ in range(na):
		leave, arrive = input().split()
		leave = tuple(map(int, leave.split(':')))
		arrive = tuple(map(int, arrive.split(':')))
		trains.append((leave, arrive, 0))
	for _ in range(nb):
		leave, arrive = input().split()
		leave = tuple(map(int, leave.split(':')))
		arrive = tuple(map(int, arrive.split(':')))
		trains.append((leave, arrive, 1))
	trains.sort()
	# 기차 출발
	waiting = [[], []] # 각각 a역, b역.
	cnt = [0, 0]
	for leave, arrive, station in trains:
		# 현재 역에 대기중인 기차가 있을 경우
		if waiting[station] and waiting[station][0] <= leave:
			heapq.heappop(waiting[station])
			heapq.heappush(waiting[(station + 1) % 2], addTime(arrive, t))
		# 새로운 기차 출발
		else:
			heapq.heappush(waiting[(station + 1) % 2], addTime(arrive, t))
			cnt[station] += 1
# output
	print(f"Case #{case}: {cnt[0]} {cnt[1]}")