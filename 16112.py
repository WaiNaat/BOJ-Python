import heapq

# input
n, k = map(int, input().split())
quests = []
totalExp = 0
for quest in map(int, input().split()):
	totalExp += quest
	heapq.heappush(quests, quest)

# process
expLoss = 0
sol = 0
for _ in range(k):
	expLoss += heapq.heappop(quests)
	sol += totalExp - expLoss

# output
print(sol)

'''
힙은
	insert: O(log n)
	pop: O(log n)
이라서 이 알고리즘은 
	정렬 및 sum: O(n log n)
	정답 구하기: O(n log n)
이지만
v2는 sum을 따로 구한대신에 pop이 없어서 
	정렬: O(n log n)
	sum: O(n)
	정답 구하기: O(n) 
이기 때문에 훨씬 빠르다.
'''