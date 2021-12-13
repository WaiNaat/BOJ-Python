### 시간 초과 ###
'''
입력값 받을 때 이중for문이 원인으로 보임.
'''

import sys
input = sys.stdin.readline

# input
N = int(input())
chains = []
for i in range(N):
	a, b, c = map(int, input().split())
# process
	'''
	chain := [0]깨지는 화분 수, [1]연쇄 시발점, [2]깨지는 화분 번호, [3]깨지는 숫자

	i번째 화분에 대해
		기존 연쇄반응 중 i번째 화분이 같이 깨지는 게 있다면 거기에 추가
		없으면 i번째 화분이 새로운 연쇄반응의 시발점
	가장 많이 깨지는 연쇄반응 순서대로 깸(연쇄반응 시발점이 이미 깨진 화분이면 제외)
	'''
	# 연쇄반응 만들기
	chained = False
	for chain in chains:
		if a in chain[3] or b in chain[3] or c in chain[3]:
			chain[0] += 1
			chain[2].add(i)
			chain[3].update([a, b, c])
			chained = True
	
	if not chained:
		chain = [1, i, set([i]), set([a, b, c])]
		chains.append(chain)
# 화분 깨지는 숫자 내림차순 정렬
chains.sort(reverse=True)
# 화분 깨기
pots = set([i for i in range(N)])
cnt = 0
for chain in chains:
	if chain[1] in pots: # chain의 시작점이 아직 깨지지 않음
		pots -= chain[2]
		cnt += 1
	if not pots: break

# output
print(cnt)