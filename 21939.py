import sys, heapq
input = sys.stdin.readline
'''
이중 우선순위 큐 문제.
최소 힙 1개, 최대 힙 1개.
문제 리스트에 남아 있는 문제들의 사전 1개.
	(최소 힙과 최대 힙 간의 동기화를 위함)
	key: 문제 번호, value: 난이도
'''
h_min = []
h_max = []
problems = {}
# 문제 입력
n = int(input())
for _ in range(n):
	num, hardness = map(int, input().split())
	heapq.heappush(h_max, (-hardness, -num))
	heapq.heappush(h_min, (hardness, num))
	problems[num] = hardness

m = int(input())
for _ in range(m):
	# 명령 입력
	command = input().split()
	# 명령 실행
	if command[0] == "recommend":
		num = hardness = 0
		if command[1] == '1':
			while num not in problems or problems[num] != hardness:
				hardness, num = map(lambda x: -int(x), heapq.heappop(h_max))
			heapq.heappush(h_max, (-hardness, -num))
		else:
			while num not in problems or problems[num] != hardness:
				hardness, num = heapq.heappop(h_min)
			heapq.heappush(h_min, (hardness, num))
		print(num)
	elif command[0] == "add":
		num, hardness = map(int, (command[1], command[2]))
		heapq.heappush(h_max, (-hardness, -num))
		heapq.heappush(h_min, (hardness, num))
		problems[num] = hardness
	else: # solved
		problems.pop(int(command[1]))