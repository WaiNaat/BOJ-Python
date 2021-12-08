import sys
input = sys.stdin.readline
import heapq

# input
N = int(input())

# process
'''
prize_sum := i번째 대회까지의 (최소) 상금합
prize_list := 참가한 대회들의 상금 목록
pass_cnt := 참가하지 못한 대회 수

i+1번째 대회에서 x_i < prize_sum 이라 대회에 참가하지 못할 경우
	참가했던 대회들 중 최대 상금의 대회를 포기했을 때 i+1 대회에 참가할 수 있는지 확인
	포기하면 참가할 수 있고 그 때 상금합이 더 작아진다면 포기하고 참가
	아니면 i+1번째 대회는 패스
'''
prize_sum = pass_cnt = 0
prize_list = []

for i in range(N):
	x, p = map(int, input().split())
	if x < prize_sum:
		discard = prize_sum + prize_list[0]
		if discard <= x and discard + p < prize_sum:
			pass_cnt += 1
			prize_sum = discard + p
			heapq.heappop(prize_list)
			heapq.heappush(prize_list, -p) # heapq는 최소 힙이라 음수화해서 저장
		else:
			pass_cnt += 1
	else:
		prize_sum += p
		heapq.heappush(prize_list, -p)
	if pass_cnt >= 2: break

# output
print("Kkeo-eok") if pass_cnt < 2 else print("Zzz")