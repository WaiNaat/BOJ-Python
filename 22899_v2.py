### 65점 ###
'''
65점이면 시간 초과라는 뜻 아님??
'''

import heapq
# input
n, k = map(int, input().split())
A = map(int, input().split())
B = map(int, input().split())
# process
'''
1. 각 출제자별로 문제 준비 시간을 저장하는 최소 힙 n개.
2. 현재 출제된 문제들을 모으는 최대 힙 1개.

L=i일 경우
	모든 출제자가 i개의 문제를 제출한다. 총 문제는 i*n개.
	i*n > k면 출제된 문제들에서 비싼 문제를 빼서 k개를 맞춘다.
	이러면 각 출제자는 최대 i개의 문제를 만들되 문제의 합은 k개고
	그 비용의 합은 최소가 된다.
L=i+1일 경우
	L=i인 경우의 답에 모든 출제자가 한 개씩 더 제출해서 같은 방식으로.

cnt := 출제한 문제 수
e_cnt := 아직 문제를 더 출제할 수 있는 출제자 수
'''
# 출제자별 문제 준비 시간.
examiner = {}
for a, b in zip(A, B):
	if a - 1 not in examiner: examiner[a - 1] = []
	heapq.heappush(examiner[a - 1], b)
# L값별로 계산.
sol = [0 for _ in range(n)]
cnt = time = 0
e_cnt = n
questions = []
for L in range(1, n + 1):
	# 출제자가 최후의 1인만 남았을 경우:
	# 이미 k개를 채웠다면 굳이 더 할 필요 없음.
	if e_cnt == 1 and cnt == k:
		sol[L - 1] = sol[L - 2]
	# 1개씩 제출.
	for e in list(examiner.keys()):
		cnt += 1
		q = heapq.heappop(examiner[e])
		heapq.heappush(questions, -q)
		time += q
		if not examiner[e]:
			e_cnt -= 1
			examiner.pop(e)
	# 모든 출제자가 L개만큼 제출했는데 모자랄 경우
	if cnt < k:
		sol[L - 1] = -1
		continue
	# k개 맞추는 과정
	while cnt > k:
		q = -heapq.heappop(questions)
		time -= q
		cnt -= 1
	sol[L - 1] = time
# output
print(*sol)