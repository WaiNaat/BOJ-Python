### 시간 초과 ###

# functions
def biSearch(value):
	'''
	product 배열에 value값이 있으면 True, 없으면 False 반환
	'''
	left = 0
	right = len(product)
	while left < right:
		mid = (left + right) // 2
		if product[mid] == value:
			return True
		elif product[mid] < value:
			left = mid + 1
		else:
			right = mid
	return False

# input
n, c = map(int, input().split())
product = list(map(int, input().split()))
# process & output
'''
일단 정렬
이분 탐색으로 정확히 c인 물건이 있나 확인
없으면 임의로 1개를 고른 후 c - p1인 물건이 있나 확인
이래도 없으면 임의로 2개를 고른 후 c - p1 - p2인 물건이 있나 확인
'''
product.sort()
found = 0
# 1개만 고르기
if biSearch(c):
	found = 1
# 2개 고르기
for p1 in product:
	if found == 1:
		break
	# 두 번째 상품인 val이 p1과 같은 상품이면 안 됨
	val = c - p1
	if val > 0 and val != p1 and biSearch(val):
		found = 1
	# 3개 고르기
	else:
		for p2 in product:
			if p1 == p2:
				continue
			val = c - p1 - p2
			# 세 번째 상품인 val이 기존 p1, p2와 같은 상품이면 안 됨
			if val > 0 and val != p1 and val != p2 and biSearch(val):
				found = 1
# output
print(found)