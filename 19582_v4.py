import sys
input = sys.stdin.readline

# input
N = int(input())

# process
'''
prize_sum := i번째 대회까지의 (최소) 상금합
prize_max := i번째 대회들 중 최대 상금
pass_cnt := 참가하지 못한 대회 수

i+1번째 대회에서 x_i < prize_sum 이라 대회에 참가하지 못할 경우
	참가했던 대회들 중 최대 상금의 대회를 포기했을 때 i+1 대회에 참가할 수 있는지 확인
	포기하면 참가할 수 있고 그 때 상금합이 더 작아진다면 포기하고 참가
	아니면 i+1번째 대회는 패스

prize_max값을 사용한다는 뜻은 한 번 패스한다는 뜻.
두 번 패스하면 참을 수 없다 했으니 두 번째 prize_max값 이용부터는 오류가 나도 상관이 없음.
즉 heap을 이용해서 이전 대회 포기 이후의 최대 상금 값을 쉽게 구한다는 생각 << 이럴 필요조차 없음.
'''
prize_sum = prize_max = pass_cnt = 0

for i in range(N):
	x, p = map(int, input().split())
	if x < prize_sum:
		discard = prize_sum - prize_max
		if discard <= x and discard + p < prize_sum:
			prize_sum = discard + p
		pass_cnt += 1
		if pass_cnt >= 2: break
	else:
		prize_sum += p
		if p > prize_max: prize_max = p

# output
print("Kkeo-eok") if pass_cnt < 2 else print("Zzz")