import sys
input = sys.stdin.readline

a, b = map(int, input().split())
fib = [1, 2]
max_fib = 2
while a != 0 or b != 0:
	# 현재 fib 배열이 b보다 작으면 숫자를 채움
	while max_fib <= b:
		max_fib = fib[-1] + fib[-2]
		fib.append(max_fib)
	# 숫자 세기
	cnt = 0
	for val in fib:
		if a <= val <= b:
			cnt += 1
		
	print(cnt)

	a, b = map(int, input().split())