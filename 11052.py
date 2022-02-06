# input
n = int(input())
p = tuple(map(int, input().split()))
# process
'''
민규 씨가 사는 카드가 i개일 때 최대 비용을 opt(i)라 하면
opt(i) =
	opt(i-1) + p(1)
	opt(i-2) + p(2)
	...
	opt(i-i) + p(i)
	중 최댓값.
'''
opt = [0 for _ in range(n + 1)]
opt[1] = p[0]

for i in range(2, n + 1):
	val = 0
	for j in range(1, i + 1):
		tmp = opt[i - j] + p[j - 1]
		if val < tmp:
			val = tmp
	opt[i] = val

# output
print(opt[n])