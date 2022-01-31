import sys
input = sys.stdin.readline
# input
n = int(input())
wine = [int(input()) for _ in range(n)]
# process
'''
!연속으로 놓인 3잔을 마실 수 없음!
i번 포도주의 양을 wine(i),
0번~i번 포도주들을 마셨을 때 최대 총량을 opt(i)라 하면
opt(i) =
	opt(i-1)  (i번 포도주 안 마심)
	wine(i) + wine(i-1) + opt(i-3)  (i-2번 포도주 안 마심)
	wine(i) + opt(i-2)  (i-1번 포도주 안 마심)
	중 최대인 값.
'''
opt = [0 for _ in range(n)]
opt[0] = wine[0]
if n > 1: opt[1] = wine[0] + wine[1]
if n > 2: opt[2] = max(opt[1], wine[1] + wine[2], wine[0] + wine[2])

for i in range(3, n):
	tmp1 = wine[i] + wine[i - 1] + opt[i - 3]
	tmp2 = wine[i] + opt[i - 2]
	opt[i] = max(opt[i - 1], tmp1, tmp2)
# output
print(opt[n - 1])