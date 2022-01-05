import sys
input = sys.stdin.readline
import heapq
# input & process
'''
계산대별로 끝나는 시간을 기억하는 힙.
	최소 힙: 끝나는 시간이 빠를수록 다음사람의 대기시간이 적음.
	우선순위: 1순위 끝나는 시간, 2순위 계산대 번호
손님별로 끝나는 시간을 기억하는 힙.
	우선순위: 1순위 끝나는 시간 작은 순, 2순위 계산대 번호 높은 순.

counter := 위에서 말한 계산대별 힙. [0]끝나는시간 [1]계산대번호
customer := 위에서 말한 손님별 힙. [0]끝나는시간 [1]계산대번호 [2]id
'''
counter = []
customer = []

n, k = map(int, input().split())
for i in range(k): heapq.heappush(counter, [0, i])

# 손님 입장
for _ in range(n):
	customer_id, w = map(int, input().split())
	# 가장 대기시간이 적은 카운터로 안내
	time, counter_id = heapq.heappop(counter)
	time += w
	heapq.heappush(counter, [time, counter_id])
	heapq.heappush(customer, [time, -counter_id, customer_id])
# 손님 퇴장
sol = 0
for i in range(1, n + 1):
	_, _, id = heapq.heappop(customer)
	sol += i * id
# output
print(sol)