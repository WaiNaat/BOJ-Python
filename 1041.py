# input
n = int(input())
a, b, c, d, e, f = map(int, input().split())

# process
'''
주사위를 쌓았을 때 총 세 가지 경우
1. 위쪽 꼭짓점 4개: 3면 노출
2. 모서리 (n-1)*4 + (n-2)*4개: 2면 노출
3. 면 (n-2)^2 * 5 + (n-2)*4개: 1면 노출
각 경우에서 최솟값들을 찾아서 더하면 됨.
'''
sol = 0
# 3면 노출
tmp = min(a + d + e, 
		a + c + e,
		a + b + d,
		a + b + c,
		b + f + d,
		b + f + c,
		e + f + d,
		e + f + c
		)
sol += tmp *  4

# 2면 노출
tmp = min(e + d, e + a, e + c,
		a + d, a + c, a + b,
		b + d, b + c, b + f,
		f + d, f + c, f + e
		)
sol += tmp * ((n - 1) * 4 + (n - 2) * 4)

# 1면 노출
tmp = min(a, b, c, d, e, f)
sol += tmp * ((n - 2) ** 2 * 5 + (n - 2) * 4)

# 예외 처리: n=1일 때
if n == 1:
	sol = sum([a, b, c, d, e, f]) - max(a, b, c, d, e, f)

# output
print(sol)