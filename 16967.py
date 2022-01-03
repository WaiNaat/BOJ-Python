import sys
input = sys.stdin.readline
# input
height, width, X, Y = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(height + X)]
# process
'''
1. range(x)의 행과 range(y)의 열은 원본 그대로임.
2. 나머지는 A[i, j] = B[i, j] - A[i-x, j-y] 를 만족.
'''
A = [[0 for _ in range(width)] for _ in range(height)]
# 1.
for i in range(X):
	for j in range(width):
		A[i][j] = B[i][j]
for j in range(Y):
	for i in range(height):
		A[i][j] = B[i][j]
# 2.
for i in range(X, height):
	for j in range(Y, width):
		A[i][j] = B[i][j] - A[i - X][j - Y]
# output
for line in A: print(*line)