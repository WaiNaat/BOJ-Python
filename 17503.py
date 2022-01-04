import sys
input = sys.stdin.readline
# function
def drink(liver):
	'''
	간 레벨 x 이하의 맥주 중 선호도 높은 거 n개의 합 반환.
	'''
	global n
	left = 1
	right = len(beer)
	while left < right:
		mid = (left + right) // 2
		if beer[mid][1] <= liver: left = mid + 1
		else: right = mid
	if left < n: return -1 # 술이 모자람.
	drinkable = sorted(beer[:left], key=lambda x: -x[0])
	ret = 0
	for i in range(n):
		ret += drinkable[i][0]
	return ret

# input
n, m, k = map(int, input().split())
beer = [tuple(map(int, input().split())) for _ in range(k)]
# process
'''
움직여야 하는 값은 간 레벨.
간 레벨 x 이하의 맥주 중 선호도 높은 거 n개의 합이
합 < m: x를 높여야 함.
합 >= m: x를 낮춰야 함.

beer := 도수 레벨 오름차순으로 정렬한 배열.
'''
beer.sort(key=lambda x: x[1])
left = 1
right = 2147483648
while left < right:
	mid = (left + right) // 2
	if drink(mid) < m: left = mid + 1
	else: right = mid
if left == 2147483648: left = -1
# output
print(left)