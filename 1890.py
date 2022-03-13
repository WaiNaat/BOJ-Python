import sys
input = sys.stdin.readline

# input
n = int(input())
board = [tuple(map(int, input().split())) for _ in range(n)]

# process
'''
opt(i, j)를 board[i][j]로 갈 수 있는 경로의 개수라 하면
opt(i + board[i][j], j) += opt(i, j)
opt(i, j + board[i][j]) += opt(i, j)
이런 식으로 opt배열 업데이트 해주면 됨
'''
opt = [[0 for _ in range(n)] for _ in range(n)]
opt[0][0] = 1

for i in range(n):
	for j in range(n):
		
		if i == j == n - 1:
			break

		d = board[i][j]

		if j + d < n:
			opt[i][j + d] += opt[i][j]
		if i + d < n:
			opt[i + d][j] += opt[i][j]

# output
print(opt[-1][-1])