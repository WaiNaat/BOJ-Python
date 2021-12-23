import sys
input = sys.stdin.readline
# input
height, width = map(int, input().split())
rectangle = [input().rstrip() for _ in range(height)]
# process
'''
max(N)=max(M)=50이므로
O(NM^2) 완전탐색 알고리즘 사용 가능.

각 가로줄에서 두 개의 숫자를 고른다.
이걸로 조건을 만족하는 정사각형을 만들 수 있는지 확인한다.
	이 때 윗단계에서 고른 두 숫자가 정사각형의 윗변이 됨.
아래 줄로 내려가서 반복.
'''
square = 1
for h in range(height - 1):
	for w in range(width - 1):
		top_left = rectangle[h][w]
		for w2 in range(w, width):
			if top_left == rectangle[h][w2]: # 정사각형 윗변 완성
				size = w2 - w
				# 정사각형을 만들 수 있는지 검사
				if size >= height - h: continue
				if top_left == rectangle[h + size][w] \
					and top_left == rectangle[h + size][w2]:
					square = max(square, size + 1)
# output
print(square ** 2)