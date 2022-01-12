import sys
input = sys.stdin.readline
# input
n = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(n)]
# process
'''
각 날짜별로 몇 개의 일정이 겹치는지 센다 = 세로 길이
일정이 없는 날과 일정이 없는 날 사이의 길이 = 가로 길이
'''
calendar = [0 for _ in range(367)]
for start, end in schedule:
	for i in range(start, end + 1):
		calendar[i] += 1

x = y = sol = 0
for i in range(1, 367):
	if calendar[i] == 0:
		sol += x * y
		x = y = 0
	else:
		x += 1
		y = max(y, calendar[i])
# output
print(sol)