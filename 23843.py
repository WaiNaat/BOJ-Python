import heapq
# input
n, m = map(int, input().split())
t = input().split()
# process
'''
제일 오래 걸리는 전자기기부터 미리 충전기에 꼽아야 함.
>> 전자기기들의 최대 힙.
다음 전자기기는 충전기들 중 가장 충전이 빨리 끝나는 데 꼽아야 함.
>> 충전 종료 시간 최소 힙.
'''
# 힙 제작
charger = [0 for _ in range(m)]
t = list(map(lambda x: -int(x), t))
heapq.heapify(t)
# 충전 시작
while t:
	heapq.heappush(charger, heapq.heappop(charger) - heapq.heappop(t))
# output
print(max(charger))