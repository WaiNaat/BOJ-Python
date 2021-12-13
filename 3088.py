### 틀렸습니다 ###
'''
1-2-4-5가 연쇄 가능할 때 이 방법을 쓰면
1-2, 4-5로 나눠서 깨야 함
'''

import sys
input = sys.stdin.readline

# input
N = int(input())
cnt = 0
crash = set([])
for _ in range(N):
	a, b, c = map(int, input().split())
# process
	'''
	crash := 화분이 이 안의 숫자와 겹치면 깨진다.

	i번째 화분에 대해
	1. 이전에 연쇄적으로 깨지던 화분의 'crash'와 겹치는 게 하나도 없다
		>> i번째 화분을 직접 깨고, 'crash'를 초기화하고 i번째 화분의 숫자로 채운다. 
	2. 이전에 화분이 연쇄적으로 깨지고 있었고, i번째 화분도 깨진다
		>> 깨지게 냅두고 'crash'에 i번째 화분의 숫자도 추가한다.
	'''
	if a not in crash and b not in crash and c not in crash:
		cnt += 1
		crash = set([a,b,c])
	else:
		crash.add(a)
		crash.add(b)
		crash.add(c)
# output
print(cnt)