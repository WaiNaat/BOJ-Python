import sys
input = sys.stdin.readline
# input
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
# process
while n > 1:
	# 222-풀링 1회 실행
	aux = []
	for row in range(0, n, 2):
		aux_row = []
		for col in range(0, n, 2):
			square = [matrix[row][col], matrix[row][col + 1], matrix[row + 1][col], matrix[row + 1][col + 1]]
			square.sort()
			aux_row.append(square[-2])
		aux.append(aux_row)
	matrix = aux
	n //= 2
# output
print(matrix[0][0])