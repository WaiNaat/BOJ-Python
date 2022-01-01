### 시간 초과 ###

import sys
input = sys.stdin.readline
# input
m = int(input())
arr = [0]
for _ in range(m):
	query = tuple(map(int, input().split()))
# process & output
	if query[0] == 1:
		arr.append(query[1])
	elif query[0] == 2:
		arr.remove(query[1])
	elif query[0] == 3:
		print(sum(arr))
	else:
		result = arr[0] if arr else 0
		for i in range(1, len(arr)): result ^= arr[i]
		print(result)