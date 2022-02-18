import sys
sys.setrecursionlimit(10 ** 6)
# function
def draw(row, col, size):
	# base case
	if size == 3:
		canvas[row][col] = '*'
		for i in (-1, 1):
			canvas[row + 1][col + i] = '*'
		for i in range(-2, 3):
			canvas[row + 2][col + i] = '*'
		return
	# recursive step
	size //= 2
	draw(row, col, size)
	draw(row + size, col - size, size)
	draw(row + size, col + size, size)

# input
n = int(input())
# process
'''
일단 맨 마지막 줄 맨 오른쪽엔 공백이 없어야 함.
	>> 출력 직전에 처리
별을 찍는 부분을 통째로 도화지처럼 2차원 배열로 만든 후
작은 삼각형의 위쪽 꼭짓점 3개 기준으로 각각 재귀하면 된다.
'''
canvas = [[' ' for _ in range(2 * n)] for _ in range(n)]
draw(0, n - 1, n)
# output
canvas[n - 1].pop()
for line in canvas:
	print(''.join(line))