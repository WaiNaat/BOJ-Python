import sys
input = sys.stdin.readline
import heapq
# input
n, centi, t = map(int, input().split())
giants = []
for _ in range(n): heapq.heappush(giants, -int(input()))
# process
'''
최대 힙으로 뿅망치 t번 먹이고 제일 키 큰 거인과 비교.
'''
hammer = lambda x: max(1, x // 2)
hammer_cnt = 0
centi_biggest = True if centi > -giants[0] else False
for _ in range(t):
	if centi_biggest: break
	heapq.heappush(giants, -hammer(-heapq.heappop(giants)))
	hammer_cnt += 1
	if centi > -giants[0]: centi_biggest = True
# output
print(f"YES\n{hammer_cnt}" if centi_biggest else f"NO\n{-giants[0]}")