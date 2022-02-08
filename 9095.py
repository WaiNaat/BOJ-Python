import sys
input = sys.stdin.readline
# input
t = int(input())
opt = [0, 1, 2, 4]
for _ in range(t):
	n = int(input())
# process
	'''
	본인보다 1 작은 수에 1을 더하고, 2 작은 수에 2를, 3 작은 수에 3을 더하면 본인.
	opt(i)를 i를 1, 2, 3의 합으로 나타내는 법이라 하면
	opt(i) = opt(i-1) + opt(i-2) + opt(i-3)
	'''
	while n > len(opt) - 1:
		opt.append(opt[-1] + opt[-2] + opt[-3])
# output
	print(opt[n])