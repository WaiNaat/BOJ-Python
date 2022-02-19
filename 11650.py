import sys
input = sys.stdin.readline
# input
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
# process
points.sort()
# output
for point in points:
	print(*point)