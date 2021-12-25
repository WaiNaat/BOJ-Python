# input
S, K = map(int, input().split())
# process
'''
곱이 최대가 되려면 K개로 나눈 조각들의 크기가
최대한 비슷해야 한다.
'''
base, rest = divmod(S, K)
sol = 1
for _ in range(K):
	if rest > 0:
		sol *= base + 1
		rest -= 1
	else:
		sol *= base
# output
print(sol)