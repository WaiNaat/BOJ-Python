# input
n = int(input())
A = list(map(int, input().split()))

# process
'''
opt(n)을 A[0]~A[n]의 부분수열 중 바이토닉~~ 이라고 하되
opt(n, increasing)이면 현재 증가하는 중이라는 뜻이고,
opt(n, decreasing)이면 현재 감소하는 중이라는 뜻.

opt(n, increasing) = 
	1  (본인이 시작점)
	opt(m, increasing) + 1  (m은 m<n이고 A[m]<A[n]인 m 중 opt(m)이 최대인 m)
둘 중 큰 값

opt(n, decreasing) =
	1  (본인이 시작점)
	opt(m, increasing) + 1
	opt(m, decreasing) + 1  (m은 m<n이고 A[m]>A[n]인 m 중 opt(m)이 최대인 m)
셋 중 큰 값
'''
opt_inc = [0 for _ in range(n)]
opt_dec = [0 for _ in range(n)]
sol = 1

for i in range(n):
	for j in range(0, i):
		# opt_inc 계산
		if A[j] < A[i] and opt_inc[j] > opt_inc[i]:
			opt_inc[i] = opt_inc[j]
		# opt_dec 계산
		if A[j] > A[i] and opt_inc[j] > opt_dec[i]:
			opt_dec[i] = opt_inc[j]
		if A[j] > A[i] and opt_dec[j] > opt_dec[i]:
			opt_dec[i] = opt_dec[j]
	opt_inc[i] += 1
	opt_dec[i] += 1
		
# output
print(max(max(opt_inc), max(opt_dec)))