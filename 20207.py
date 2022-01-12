### 틀렸습니다 ###

import sys, heapq
input = sys.stdin.readline
# input
n = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(n)]
# process
'''
일정 시작일 오름차순 정렬(끝나는 날은 내림차순).
힙을 이용해서 '연속된 일정'을 코팅지 하나로 덮는 묶음을 만들 거임.
	일정 끝나는 날 최소 힙.
만약 새로운 일정이 기존 연속된 일정과 겹치는 부분이 있으면
	기존 연속된 일정에 추가하는데 이 때
	힙의 뿌리랑 겹치지 않으면 거기에 추가,
	아니면 새로운 줄에 추가(힙에 새롭게 삽입).
겹치는 부분이 없으면 기존 연속된 일정에 대한 코팅지 크기 계산,
새로운 코팅지 시작.

sche_end := 현재 일정 묶음이 끝나는 날.
'''
schedule.sort(key = lambda x: (x[0], -x[1]))
schedule.append((366, 366))
h = []
sche_start = sche_end = sol = 0
for s in schedule:
	# s가 현재 연속된 일정 그룹에 속해있는 경우
	if h and sche_end + 1 >= s[0]:
		if h[0] < s[0]:
			heapq.heapreplace(h, s[1])
		else:
			heapq.heappush(h, s[1])
		sche_end = max(sche_end, s[1])
	# s는 새로운 연속된 일정 그룹인 경우
	else:
		sol += len(h) * (sche_end - sche_start + 1)
		h = [s[1]]
		sche_start, sche_end = s
# output
print(sol)