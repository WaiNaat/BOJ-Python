# input
n = int(input())
A = tuple(map(int, input().split()))

# process
'''
opt(i)를 A[0]~A[i]에서 A[i]를 포함한 가장긴감소하는부분수열의길이라 하면
opt(i) = 
	1   (본인이 그 부분수열의 시작)
	max(opt(j)) + 1   (j<i, A[j]>A[i])
'''
opt = [0 for _ in range(n)]

for i in range(n):

	for j in range(i):
		if opt[i] < opt[j] and A[j] > A[i]:
			opt[i] = opt[j]
	
	opt[i] += 1

# output
print(max(opt))