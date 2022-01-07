import heapq

n = int(input())
decks = []
for i in range(n):
	heapq.heappush(decks, int(input()))

sol = 0
for i in range(n-1):
	combined_deck = heapq.heappop(decks) + heapq.heappop(decks)
	sol += combined_deck
	heapq.heappush(decks, combined_deck)

print(sol)

