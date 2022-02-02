# input
n = int(input())
# process
'''
i 크기의 직사각형을 채우는 방법의 수를 opt(i)라 하면
i-1 크기의 직사각형에 2*1짜리 하나를 붙이거나
i-2 크기의 직사각형에 1*2 두 개 또는 2*2 한 개를 붙이면 된다.
opt(i) = opt(i-1) + 2 * opt(i-2)
'''
opt = [None for _ in range(n + 1)]
opt[1] = 1
if n > 1: opt[2] = 3
for i in range(3, n + 1):
	opt[i] = (opt[i - 1] + 2 * opt[i - 2]) % 10007
# output
print(opt[n])