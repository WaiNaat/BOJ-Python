def gcd(m, n):
	if m < n : m, n = n, m
	while n != 0: m, n = n, m % n
	return m

n, m = tuple(map(int, input().split(':')))
div = gcd(n, m)
print("%d:%d" % (int(n / div), int(m/div)))

