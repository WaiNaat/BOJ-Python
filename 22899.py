### 35점 ###
'''
>> 시간을 줄여야 한다는 뜻
'''

import heapq, copy
# input
n, k = map(int, input().split())
A = map(int, input().split())
B = map(int, input().split())
# process
'''
1. 각 출제자별로 문제 준비 시간을 저장하는 최소 힙 n개.
2. 각 출제자별로 현재 몇 문제를 출제했는지 저장하는 배열 1개.
3. 각 출제자들의 준비 시간이 가장 짧은 문제들을 저장하는 최소 힙 1개.

3번 힙에서 하나씩 빼서 출제.
이 때 출제한 사람이 아직 L개만큼 출제 안 했으면
	해당 출제자의 1번 힙에서 하나를 빼서 3번 힙에 넣음.
'''
# 출제자들의 문제 준비 시간.
examiner_init = [[] for _ in range(n)]
for a, b in zip(A, B):
	heapq.heappush(examiner_init[a - 1], b)
# 출제자들의 문제 출제 개수.
made_question_num_init = [1 for _ in range(n)]
# 준비 시간이 가장 짧은 문제들.
waiting_init = []
for i in range(n):
	if examiner_init[i]:
		heapq.heappush(waiting_init, (heapq.heappop(examiner_init[i]), i))

# L값별로 계산.
sol = [-1 for _ in range(n)]
for L in range(1, n + 1):
	if L >= k: sol[L - 1] = sol[k - 1]
	time = 0
	cnt = 0
	examiner = copy.deepcopy(examiner_init)
	made_question_num = made_question_num_init.copy()
	waiting = copy.deepcopy(waiting_init)

	while cnt < k:
		if not waiting:
			time = -1
			break
		t, a = heapq.heappop(waiting)
		time += t
		cnt += 1
		if made_question_num[a] < L and examiner[a]:
			heapq.heappush(waiting, (heapq.heappop(examiner[a]), a))
			made_question_num[a] += 1
	sol[L - 1] = time

# output
print(*sol)