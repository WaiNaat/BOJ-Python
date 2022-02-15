from collections import deque
# function
def shuffle(deck, k):
	deck = deque(deck)
	result = deque()
	# i번째 단계
	for i in range(1, k + 2):
		aux = deque()
		# 위로 올리는 카드를 aux에 저장
		for _ in range(2 **  (k - i + 1)):
			aux.appendleft(deck.pop())
		# 더미에 남은 카드는 result로 옮김
		while deck:
			result.appendleft(deck.pop())
		deck = aux.copy()
	while deck:
		result.appendleft(deck.pop())
	return result

# input
n = int(input())
after_shuffle = tuple(map(int, input().split()))
# process
'''
카드 더미의 위로 가는 숫자를 따로 모아서 섞은 후의 더미를 구할 수 있음
'''
k1 = k2 = 1
while 2 ** k1 < n:
	while 2 ** k2 < n:
		deck = [i for i in range(1, n + 1)]
		result = shuffle(shuffle(deck, k1), k2)
		isSolution = True
		for i in range(n):
			if after_shuffle[i] != result[i]:
				isSolution = False
				break
		if isSolution:
			break
		k2 += 1
	if isSolution:
		break
	k1 += 1
	k2 = 1
# output
print(k1, k2)