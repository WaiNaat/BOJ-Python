import sys
input = sys.stdin.readline
# input
m = int(input())
sum_val = 0
xor_val = 0
for _ in range(m):
	query = tuple(map(int, input().split()))
# process & output
	'''
	수열의 순서는 지킬 필요가 없다.
	애초에 수열일 필요가 없음.
	출력값은 결국 합 아니면 xor니까.
	xor의 역연산은 xor?
	'''
	if query[0] == 1:
		sum_val += query[1]
		xor_val ^= query[1]
	elif query[0] == 2:
		sum_val -= query[1]
		xor_val ^= query[1]
	elif query[0] == 3:
		print(sum_val)
	else:
		print(xor_val)