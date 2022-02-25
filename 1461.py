# input
n, m = map(int, input().split())
coords = list(map(int, input().split()))

# process
'''
'마지막에' 놓아야 하는 책들부터 역산.
항상 남은 책들의 좌표 합이 최소가 되게!
	>> 가장 먼 거리의 책 m개를 마지막에 놓아야 함.

이동 경로 중간에 원점이 있으면 손해
	>> 양의 좌표와 음의 좌표로 나눠서 확인.
'''
# 양의 좌표 책과 음의 좌표 책으로 분리
positive_books = []
negative_books = []

for c in coords:
	if c < 0:
		negative_books.append(c)
	else:
		positive_books.append(c)

positive_books.sort()
negative_books.sort(reverse = True)

# 양의 좌표와 음의 좌표를 확인해서 가장 먼 거리인 책들 처리
sol = 0
while positive_books or negative_books:
	dist_p = positive_books[-1] if positive_books else -1
	dist_n = abs(negative_books[-1]) if negative_books else -1

	faraway = positive_books if dist_p > dist_n else negative_books
	for _ in range(m):
		if not faraway: break
		faraway.pop()
	
	if sol == 0:
		sol = -max(dist_p, dist_n)
	sol += 2 * max(dist_p, dist_n)

# output
print(sol)