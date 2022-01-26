# input
n = int(input())
A = tuple(map(int, input().split()))
# process
'''
opt(n)을 A[n]을 포함하는 가장 긴 증가하는 ~~의 길이라 하면
opt(n) = 
	1 (본인이 가장 긴 ~~의 시작점)
	opt(m) + 1 (m은 m < n, A[m] < A[n]이고 opt(m)이 최대)
	중 큰 값.
'''
opt = [0 for _ in range(n)]
sol = 0
for i in range(n):
	max_opt_val = 0
	for j in range(i):
		if A[j] < A[i] and opt[j] > max_opt_val:
			max_opt_val = opt[j]
	opt[i] = max_opt_val + 1
	
	if sol < max_opt_val + 1:
		sol = max_opt_val + 1
# output
print(sol)