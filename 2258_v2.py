'''
가격 오름차순, 무게 내림차순으로 정렬

핵심은 고기를 샀을 때 그 가격 "미만"의 보너스를 얻는다는 거

1. 지금 가진 돈으로 고기를 샀을 때 덤이랑 합쳤는데도 모자라면
   같은 금액으로 살 수 있는 고기를 하나씩 더 사본다
   살 수 있으면 정답에 반영
2. 이래도 안되면 지금 가진 돈을 늘린다.
'''
import sys
input = sys.stdin.readline

# input
N, M = map(int, input().split())
meat = [tuple(map(int, input().split())) for _ in range(N)] #(무게, 가격)

# process
meat.sort(key=lambda x: (x[1], -x[0]))

sol = float('inf')
same_price_cnt = 0
same_price_weight = 0
current_price = -1
bonus = 0

for weight, price in meat:
	
	if price != current_price:
		bonus += same_price_weight
		same_price_cnt = 0
		same_price_weight = 0
		current_price = price

	same_price_cnt += 1
	same_price_weight += weight

	if same_price_weight + bonus >= M:
		sol = min(current_price * same_price_cnt, sol)

# output
print(sol if sol < float('inf') else -1)