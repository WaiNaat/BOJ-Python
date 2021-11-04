def binarySearch(value, left, right):
	if right < left:
		return left
	mid = int((left + right) / 2)
	if decks[mid] > value:
		return binarySearch(value, mid+1, right)
	elif decks[mid] < value:
		return binarySearch(value, left, mid-1)
	else:
		return mid


n = int(input())
decks = []
for i in range(n):
	decks.append(int(input()))

decks.sort(reverse=True)

sol = 0
for i in range(0,n-1):
	newDeck = decks.pop() + decks.pop()
	sol += newDeck
	idx = binarySearch(newDeck, 0, n-(i+1)-2)
	decks.insert(idx, newDeck)

print(sol)