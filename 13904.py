import sys
import heapq
input = sys.stdin.readline

# input
# assn:: key:day, value:max-heap of scores
# days: date until the last assignment
N = int(input())
assn = {}
days = 0
for _ in range(N):
	d, w = list(map(int, input().split()))
	if d not in assn:
		assn[d] = []
	heapq.heappush(assn[d], (-w, w))
	if d > days:
		days = d

# process
# day k: do assignment with max score where (due date)>=k 
sol = 0
for i in range(days, 0, -1):
	toDo = (0, 0)
	for j in range(i, days+1):
		if j in assn and len(assn[j]) > 0:
			candi = (j, assn[j][0][1])
			if candi[1] > toDo[1]:
				toDo = candi
	if toDo[0] > 0:
		heapq.heappop(assn[toDo[0]])
		sol += toDo[1]
	#print(toDo)

# output
print(sol)