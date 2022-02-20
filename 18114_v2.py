# input
n, c = map(int, input().split())
product = set(map(int, input().split()))
# process & output
'''
정확히 c인 물건이 있나 확인
없으면 임의로 1개를 고른 후 c - p1인 물건이 있나 확인
이래도 없으면 임의로 2개를 고른 후 c - p1 - p2인 물건이 있나 확인
'''
found = 0
# 1개 고르기
if c in product:
	found = 1
# 2개 고르기
for p1 in product:
	if found == 1:
		break
	# 두 번째 상품인 val이 p1과 같은 상품이면 안 됨
	val = c - p1
	if val != p1 and val in product:
		found = 1
	# 3개 고르기
	else:
		for p2 in product:
			if p1 == p2:
				continue
			val = c - p1 - p2
			# 세 번째 상품인 val이 기존 p1, p2와 같은 상품이면 안 됨
			if val != p1 and val != p2 and val in product:
				found = 1
# output
print(found)