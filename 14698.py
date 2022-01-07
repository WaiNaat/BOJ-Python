import heapq
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
	# input
	# store items in heap << makes list of slimes ordered.
	N = int(input())
	s = input().split()
	slimes = []
	for i in range(N):
		heapq.heappush(slimes, int(s[i]))
	
	# process
	# pick two smallest slimes and synthesize them
	# repeat until there's just one slime left.
	total_energy = 1
	for i in range(N-1):
		energy = heapq.heappop(slimes) * heapq.heappop(slimes)
		total_energy *= energy
		heapq.heappush(slimes, energy)
	
	# output
	print(total_energy % 1000000007)

