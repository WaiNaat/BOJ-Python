import sys
input = sys.stdin.readline

# input
N = int(input())
m = []
for _ in range(N):
	m.append(tuple(map(int, input().split())))

# process
m.sort(key = lambda x: (x[1], x[0]))
cnt = 0
last = -1
for i in range(N):
	if last <= m[i][0]:
		last = m[i][1]
		cnt += 1

# output
print(cnt)