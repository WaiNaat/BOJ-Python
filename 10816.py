# functions
def biSearch_left(value, left, right):
	while left < right:
		mid = (left + right) // 2
		if value <= cards[mid]: right = mid
		else: left = mid + 1
	return left

def biSearch_right(value, left, right):
	while left < right:
		mid = (left + right) // 2
		if value < cards[mid]: right = mid
		else: left = mid + 1
	return left

# input
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
values = map(int, input().split())
# process
'''
참고) bisect.bisect_left, bisect_right << 이걸 쓰면 그냥 가능함
정렬.
left := 중복된 숫자들 중 가장 왼쪽을 고르도록 이분탐색.
right := 중복된 숫자들 중 가장 오른쪽을 고르도록 이분탐색.
'''
cards.sort()
for value in values:
	left = biSearch_left(value, 0, N - 1)
	right = biSearch_right(value, 0, N - 1)
	cnt = 0
	if cards[left] == value:
		cnt = right - left
		if cards[right] == value: cnt += 1
# output
	print(cnt, end=' ')