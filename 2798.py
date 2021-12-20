from itertools import combinations

# input
N, blackJack = map(int, input().split())
cards = tuple(map(int, input().split()))

# process
'''
100C3 < 100,000,000 이므로 완전탐색 가능
'''
sol = 0
for a, b, c in combinations(cards, 3):
	result = a + b + c
	if result > blackJack: continue
	if sol < result: sol = result
	
# output
print(sol)