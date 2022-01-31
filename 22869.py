### python3 시간 초과 ###
### pypy3 맞았습니다 ###

# input
n, k = map(int, input().split())
a = tuple(map(int, input().split()))
# process
'''
j번 돌에서 i번 돌로 이동하는 데 드는 힘을 force(j, i),
i번째 돌까지 가는 데 필요한 최소 힘을 opt(i)라 하면
opt(i) = 
	min(max(opt(j), force(j, i)))  (0 <= j < i)
'''
force = lambda j, i, a: (i - j) * (1 + abs(a[i] - a[j]))
opt = [None for _ in range(n)]
opt[0] = 0
for i in range(1, n):
	opt[i] = min([max(opt[j], force(j, i, a)) for j in range(i)])
# output
print("YES" if opt[n - 1] <= k else "NO")