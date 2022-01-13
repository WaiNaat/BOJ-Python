### 시간 초과 ###

import sys
input = sys.stdin.readline
# input
n, k, q, m = map(int, input().split())
sleep = set(map(int, input().split()))
code = set(map(int, input().split()))
intervals = [map(int, input().split()) for _ in range(m)]

# process
'''
max(N)=5,000이므로 집합을 이용해서
출첵하지 못한 학생을 구하는 데 큰 시간이 걸리지 않음.
'''
code -= sleep # 자는 애들은 코드 못 보냄
check_success = set()
for c in code:
	for i in range(c, n + 3, c):
		check_success.add(i)
check_success -= sleep

sol = []
for left, right in intervals:
	interval = set([i for i in range(left, right + 1)])
	interval -= check_success
	sol.append(len(interval))
	
# output
print(*sol, sep='\n')