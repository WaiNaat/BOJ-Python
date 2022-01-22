### 틀렸습니다 ###

import sys
input = sys.stdin.readline
# input
t = int(input())
for _ in range(t):
	n = int(input())
	sol = []
	last = None
	for _ in range(n):
		word = input().rstrip()
# process
		'''
		사전순으로 가장 앞선다 >> 최대한 뒤쪽 걸 돌려야 한다.
		단어를 들어온 순서대로 쌓아 나가는데 새로 들어온 단어가
		쌓여있던 마지막 단어보다 빠를 경우
			자기를 뒤집어서 해결되면 자기를 뒤집음
			아니면 쌓여있던 마지막 단어를 뒤집음
		'''
		isReverse = '0'
		if last is not None and last > word:
			if word[::-1] > last:
				word = word[::-1]
				isReverse = '1'
			else:
				sol[-1] = '1'
		sol.append(isReverse)
		last = word
# output
	print("".join(sol))