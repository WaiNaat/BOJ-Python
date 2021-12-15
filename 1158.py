from collections import deque
import sys
print = sys.stdout.write

# input
N, K = map(int, input().split())

# process
q = deque([i for i in range(1, N + 1)])
sol = []
while q:
	q.rotate(-(K - 1))
	sol.append(q.popleft())

# output
print("<")
for i in range(N - 1):
	print("%d, " % sol[i])
print(">")