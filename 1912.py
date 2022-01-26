# input
n = int(input())
seq = tuple(map(int, input().split()))
# process
'''
수열의 n번째 숫자를 seq(n)이라 하고
opt(n)을 seq(n)을 마지막으로 하는 연속된 수들의 최대 합이라 하면
opt(n) = 
	seq(n)
	opt(n-1) + seq(n)
	중 큰 값.
'''
opt = [None for _ in range(n)]
sol = opt[0] = seq[0]
for i in range(1, n):
	opt[i] = max(seq[i], opt[i-1] + seq[i])
	if opt[i] > sol:
		sol = opt[i]
# output
print(sol)