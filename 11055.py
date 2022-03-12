# input
n = int(input())
A = list(map(int, input().split()))

# process
'''
opt(i)를 A[i]를 포함하는 A[0]~A[i]의 증가부분수열 중 최대합이라 하면
opt(i) = 
	A[i]   (본인이 증가부분수열의 시작)
	max(opt(k) + A[i])   (k<i, A[k]<A[i]인 k)
중 최댓값.
'''
opt = A.copy()

for i in range(1, n):

	tmp = 0
	for k in range(i):
		if A[k] < A[i] and tmp < opt[k] + A[i]:
			tmp = opt[k] + A[i]
	
	opt[i] = max(opt[i], tmp)

# output
print(max(opt))