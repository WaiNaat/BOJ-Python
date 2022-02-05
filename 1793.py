import sys
input = sys.stdin.readline
# input & process
opt = [1, 1, 3]
n = input().rstrip()
while n != "":
	n = int(n)
	'''
	2*i 직사각형을 채우는 방법의 수를 opt(i)라 하면
	opt(i) = opt(i-1) + 2 * opt(i-2)
	'''
	while len(opt) < n + 1:
		opt.append(opt[-1] + 2 * opt[-2])
# output
	print(opt[n])

	n = input().rstrip()