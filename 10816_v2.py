# input
N = int(input())
cards = map(int, input().split())
M = int(input())
values = map(int, input().split())
# process
'''
dictionary 이용
'''
deck = {}
for card in cards:
	if card not in deck: deck[card] = 1
	else: deck[card] += 1
for value in values:
	cnt = 0
	if value in deck: cnt = deck[value]
# output
	print(cnt, end=' ')