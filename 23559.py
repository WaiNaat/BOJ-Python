### 틀렸습니다 ###

import sys
input = sys.stdin.readline
# input & process
'''
A학식을 최대 몇 번 먹을 수 있는지 구해야 함.
	>> 다 B학식만 먹는다 치고 
	남는 돈 4천원당 A학식 1회로 강화.
그 다음엔 매일 비교해서 정하면 됨.

a_cnt := A학식을 최대로 먹을 수 있는 횟수
'''
n, x = map(int, input().split())

a_cnt = (x - n * 1000) // 4000
taste = 0
for _ in range(n):
	a, b = map(int, input().split())
	if a_cnt > 0 and a > b:
		taste += a
		a_cnt -= 1
	else:
		taste += b
# output
print(taste)