### 시간 초과 ###

import sys
input = sys.stdin.readline
# input
r, c = map(int, input().split())
words = [list(input().rstrip()) for _ in range(r)]
cnt = 0
# process
failed = False
for i in range(1, r):
	strings = set([])
	for j in range(c):
		s = ''.join([words[k][j] for k in range(i, r)])
		if s in strings:
			failed = True
			break
		strings.add(s)
	if failed: break
	cnt += 1
# output
print(cnt)