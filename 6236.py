import sys
input = sys.stdin.readline
# function
def withdraw(money):
	'''
	money만큼 인출할 때	몇 번 인출해야 하는지를 반환.
	'''
	cnt = wallet = 0
	for day in plan:
		if day > wallet:
			if day > money: return 2147483647
			cnt += 1
			wallet = money
		wallet -= day
	return cnt

# input
n, m = map(int, input().split())
plan = [int(input()) for _ in range(n)]
# process
'''
인출금액 최소: bisect_left의 원리.
x원씩 인출했을 때 총 인출횟수를 i라 하면
i > M: x를 늘린다.
i <= M: x를 줄인다.
'''
left = 1
right = sum(plan) + 1
while left < right:
	mid = (left + right) // 2
	if withdraw(mid) > m: left = mid + 1
	else: right = mid
# output
print(left)