import sys
input = sys.stdin.readline
# input
t = int(input())
opt = [[0 for _ in range(10)] for _ in range(1001)]
i = 1
opt[1] = [1 for _ in range(10)]
for _ in range(t):
	n = int(input())
# process
	'''
	opt(i, j)를 길이가 i이면서 j로 끝나는 비빌번호의 수라 하자.
	opt(i, 0) = opt(i-1, 7)
	opt(i, 1) = opt(i-1, 2) + opt(i-1, 4)
	opt(i, 2) = opt(i-1, 1) + opt(i-1, 3) + opt(i-1, 5)
	...
	opt(i, 9) = opt(i-1, 6) + opt(i-1, 8)
	이런 식으로 계산 가능.
	'''
	while i < n:
		i += 1
		opt[i][0] = opt[i - 1][7]
		opt[i][1] = opt[i - 1][2] + opt[i - 1][4]
		opt[i][2] = opt[i - 1][1] + opt[i - 1][3] + opt[i - 1][5]
		opt[i][3] = opt[i - 1][2] + opt[i - 1][6]
		opt[i][4] = opt[i - 1][1] + opt[i - 1][5] + opt[i - 1][7]
		opt[i][5] = opt[i - 1][2] + opt[i - 1][4] + opt[i - 1][6] + opt[i - 1][8]
		opt[i][6] = opt[i - 1][3] + opt[i - 1][5] + opt[i - 1][9]
		opt[i][7] = opt[i - 1][0] + opt[i - 1][4] + opt[i - 1][8]
		opt[i][8] = opt[i - 1][5] + opt[i - 1][7] + opt[i - 1][9]
		opt[i][9] = opt[i - 1][6] + opt[i - 1][8]
# output
	print(sum(opt[n]) % 1234567)