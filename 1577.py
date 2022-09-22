'''
이동하는 횟수가 정해져있으므로
항상 행이 커지는 방향 또는 열이 커지는 방향으로만 이동
opt(i, j) := (i, j)까지 오는 경로의 수
opt(i, j) = opt(i-1, j) + opt(i, j-1) 인데 경로가 있어야함

경로 존재 판단은 dict를 이용해서 가능

메모리제한 있으니까 opt를 이차원으로 하는게 아니라
행 기준으로 cur, next 두 개로
근데 이동방향도 정해져 있으니까 하나면 될듯?
'''
import sys
input = sys.stdin.readline

# input
col, row = map(int, input().split())
K = int(input())
cannot_pass = {}
for _ in range(K):
	c1, r1, c2, r2 = map(int, input().split())
	
	if r1 > r2 or c1 > c2:
		r1, r2 = r2, r1
		c1, c2 = c2, c1
	
	if (r1, c1) not in cannot_pass:
		cannot_pass[(r1, c1)] = set()
	cannot_pass[(r1, c1)].add((r2, c2))


# process
directions = ((1, 0), (0, 1))
opt = [0 for _ in range(col + 1)]
opt[0] = 1

for r in range(row + 1):
	
	for c in range(col + 1):
		# 아래 행에서 올라올 수 있는가?
		if (r - 1, c) in cannot_pass and (r, c) in cannot_pass[(r - 1, c)]:
			opt[c] = 0

		# 옆 열에서 올 수 있는가?
		if c > 0 and ((r, c - 1) not in cannot_pass or (r, c) not in cannot_pass[(r, c - 1)]):
			opt[c] += opt[c - 1]

# output
print(opt[col])