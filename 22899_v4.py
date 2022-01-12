import heapq
# input
n, k = map(int, input().split())
A = map(int, input().split())
B = map(int, input().split())
# process
'''
1. 만든 문제들이 어느 출제자의 몇 번째 문제인지 저장하는 최소 힙.
	우선순위 [0]출제자의 몇 번째 문제인지, [1]준비 시간
2. 현재 출제된 문제들의 준비 시간을 모으는 최대 힙.

L = 1일 경우
	모든 출제자가 자기가 만든 문제 중 가장 싼 문제를 제출.
	k개를 넘으면 거기서 비싼 문제부터 제거.
L = i일 경우
	모든 출제자가 자기가 만든 문제 중 가장 싼 i개를 제출.
	k개를 넘으면 거시서 비싼 문제부터 제거해서 k개를 맞춤.
	이러면 모든 출제자가 i개 이하로 제출하면서 최소 비용의 k문제 완성.
L = i+1일 경우
	모든 출제자가 자기가 만든 문제 중 i+1번째로 싼 문제를 제출.
	(이미 앞에서 i개는 L=i에서 제출했음)
	k개 개수를 맞춰줌.

made := 만든 문제들의 힙(1번 힙).
		[0]출제자의 몇 번째 문제인지, [1]준비 시간
examiner := 각 출제자별로 만든 문제들.
actual := 출제한 문제들의 준비 시간들의 힙(2번 힙).
'''
made = []
# 출제자별로 만든 문제를 정리
examiner = {}
for name, time in zip(A, B):
	if name not in examiner: examiner[name] = []
	examiner[name].append(time)
for e in examiner:
	examiner[e].sort()
# 만들어진 문제들을 하나로 정리
	for i in range(len(examiner[e])):
		heapq.heappush(made, (i + 1, examiner[e][i]))
# 계산.
sol = [-1 for _ in range(n)]
actual = []
time = 0
for i in range(1, n + 1):
	# 제출
	while made and made[0][0] <= i:
		_, t = heapq.heappop(made)
		time += t
		heapq.heappush(actual, -t)
	# 개수가 모자랄 경우
	if len(actual) < k: continue
	# 개수가 많을 경우
	while len(actual) > k:
		time += heapq.heappop(actual)
	sol[i - 1] = time
# output
print(*sol)