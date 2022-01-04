import sys
input = sys.stdin.readline
import heapq
# input
n, x = map(int, input().split())
h = []
taste = 0
for _ in range(n):
	a, b = map(int, input().split())
	if a <= b:
		taste += b
	else:
		heapq.heappush(h, (b-a, -a, -b))
# process
'''
A학식을 최대 몇 번 먹을 수 있는지 구해야 함.
	다 B학식만 먹는다 치고 남는 돈 4천원당 A학식 1회로 강화.

B학식이 A 이상으로 맛있으면 무조건 B를 먹음. << input에서 처리
A학식이 더 맛있는 경우
	A, B 사이의 격차가 클 경우 A를 먹음.(맛의 합 최대화)
	이 격차를 제1 기준으로 하는 힙.(최대 힙)

a_cnt := A학식을 최대로 먹을 수 있는 횟수
'''
a_cnt = (x - n * 1000) // 4000
while h:
	_, a, b = heapq.heappop(h)
	if a_cnt > 0:
		taste -= a
		a_cnt -= 1
	else:
		taste -= b
# output
print(taste)