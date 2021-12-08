### 틀렸습니다 ###

import sys
input = sys.stdin.readline

# input
N = int(input())
contest = []
for _ in range(N):
	contest.append(tuple(map(int, input().split())))

# process
# i번째 대회에 참가하면 i+1번째 대회를 참가할 수 없을 때: 참가하지 않음.
cnt = 0
prize_sum = 0
for i in range(N - 1):
	x, p = contest[i]
	if prize_sum + p > contest[i+1][0]:
		cnt += 1
		if cnt == 2: break
		continue
	prize_sum += p

x, p = contest[N - 1]
if prize_sum > x: cnt += 1

# output
print("Kkeo-eok") if cnt < 2 else print("Zzz")