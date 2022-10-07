### 틀렸습니다 ###
'''
3 2
1 1
1 1
2 3
'''

'''
가격 오름차순, 무게 내림차순으로 정렬

1. i원으로 살 수 있는 고기 중 제일 무거운 걸 산다.
2. i-1원으로 살 수 있는 모든 고기들의 무게 합과 더해 원하는 양이 되는지 확인한다.
3. 모자라면 돈을 더 준비한다.
'''
import sys
input = sys.stdin.readline

# input
N, M = map(int, input().split())
meat = [tuple(map(int, input().split())) for _ in range(N)]

# process
meat.sort(key=lambda x: (x[1], -x[0]))

i = 0
money = meat[0][1]
bonus = 0
found = False

while i < N:

	# 현재 고기를 사기에 돈이 모자라면 돈을 채움
	while meat[i][1] > money:
		money += 1
	
	# 현재 돈으로 살 수 있는 고기 중 제일 무거운 걸 샀을 때 필요한 양을 채우는지 확인
	if meat[i][0] + bonus >= M:
		found = True
		break

	# 못 채웠으면 해당 고기
	while i < N and meat[i][1] == money:
		bonus += meat[i][0]
		i += 1

# output
print(money if found else -1)