'''
이분탐색

상한액을 가능한 한 늘리면 자연스럽게 배정되는 예산이 가장 높아진다.

움직이는 값: 상한액
기준: 예산의 합
	예산의 합이 총 예산보다 크면 상한액 줄임
	작거나 같으면 상한액 늘림
'''
import sys
input = sys.stdin.readline

# function
def is_ok(limit, total):
	budget = 0
	
	for r in request:
		if r <= limit:
			budget += r
		else:
			budget += limit

	if budget <= total:
		return True
	return False

# input
N = int(input())
request = tuple(map(int, input().split()))
total_budget = int(input())

# process
left = 1
right = max(request) + 1

while left < right:
	mid = (left + right) // 2

	if is_ok(mid, total_budget):
		left = mid + 1
	else:
		right = mid

# output
print(left - 1)