import sys
input = sys.stdin.readline

# input
n, k = map(int, input().split())
item = [map(int, input().split()) for _ in range(n)]

# process
'''
opt(i, j)를 0번~i번 물건들을 최대무게 j인 배낭에 담을 때 최대 가치라 하면
opt(i, j) = 
	opt(i-1, j)   (i번째 물건을 넣지 않음)
	opt(i-1, j-weight(i)) + value(i)    (i번째 물건을 넣음)
둘 중 큰 값.
'''
opt = [[0 for _ in range(k + 1)] for _ in range(n)]

for i in range(n):
	weight, value = item[i]
	for j in range(k + 1):
		tmp1 = opt[i - 1][j]
		tmp2 = opt[i - 1][j - weight] + value if j - weight >= 0 else 0
		opt[i][j] = max(tmp1, tmp2)

# output
print(opt[n - 1][k])