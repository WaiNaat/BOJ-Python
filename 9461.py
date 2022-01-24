import sys
input = sys.stdin.readline
# input
t = int(input())
P = [None for _ in range(101)]
P[1] = P[2] = P[3] = 1
P[4] = P[5] = 2
first_none_idx = 6
for _ in range(t):
	n = int(input())
# process
	'''
	P(n) = P(n-5) + P(n-1)
	1 1 1 2 2  3 4 5 7 9
	'''
	if P[n] is None:
		for i in range(first_none_idx, n + 1):
			P[i] = P[i - 5] + P[i - 1]
		first_none_idx = n + 1
# output
	print(P[n])