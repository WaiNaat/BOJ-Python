import sys
input = sys.stdin.readline
import heapq as hq
from collections import deque
# input
n, m, k = map(int, input().split())
lines = [deque([]) for _ in range(m)]
for i in range(n):
	d, h = map(int, input().split())
	isDeca = True if i == k else False
	lines[i % m].append((-d, -h, i % m, isDeca))
# process
'''
1. 사원들을 일단 줄별로 분리한다. << 큐 사용
2. 선두만 모은 힙
	우선순위: 근무일수, 급한정도 내림차순 / 줄번호 오름차순
3. 한명이 화장실 이용(pop)하면 그 줄의 선두를 선두 힙에 push
4. 화장실 쓰는 사람이 데카인지 확인할 수 있는 추가 변수 필요.

lines[i] := i번째 줄 큐.
front := 선두 힙.
큐와 힙의 내용물은 튜플,
	[0]근무일수 [1]급한정도 [2]줄번호 [3]데카인지
'''
front = []
for line in lines:
	if line: hq.heappush(front, line.popleft())

cnt = 0
while True:
	# 화장실 이용
	_, _, line_num, isDeca = hq.heappop(front)
	if isDeca: break
	cnt += 1
	# 선두 힙 업데이트
	if lines[line_num]:
		hq.heappush(front, lines[line_num].popleft())
# output
print(cnt)