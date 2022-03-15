import sys
input = sys.stdin.readline

'''
opt(i, j)를 정수 i를 1,2,3의 합으로 나타내되
맨 마지막에 j를 쓰는 경우라 하면
opt(i, 1) = opt(i-1, 2) + opt(i-1, 3)
opt(i, 2) = opt(i-2, 1) + opt(i-2, 3)
opt(i, 3) = opt(i-3, 1) + opt(i-3, 2)
이렇게 구할 수 있다.
'''

# t 입력
t = int(input())

# 초기화
opt = [
	[0, 0, 0, 0],
	[0, 1, 0, 0], # 1
	[0, 0, 1, 0], # 2
	[0, 1, 1, 1]] # 21 12 3

# n 입력
for _ in range(t):
	n = int(input())

	# n값이 opt배열에 없을 경우 계산
	while len(opt) <= n:
		tmp = [0, 0, 0, 0]
		tmp[1] = (opt[-1][2] + opt[-1][3]) % 1000000009
		tmp[2] = (opt[-2][1] + opt[-2][3]) % 1000000009
		tmp[3] = (opt[-3][1] + opt[-3][2]) % 1000000009
		opt.append(tmp)
	
	# 출력
	print(sum(opt[n]) % 1000000009)