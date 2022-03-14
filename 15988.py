import sys
input = sys.stdin.readline

'''
opt(n)을 n을 1, 2, 3의 합으로 나타내는 방법의 수라 하면
n은 n-1에 1을, n-2에 2를, n-3에 3을 더해 만들 수 있으므로
opt(n) = opt(n-1) + opt(n-2) + opt(n-3)

만약 들어온 값이 opt배열에 없으면 생길때까지 추가 연산.
'''

# t 입력
t = int(input())

# 초기화
opt = [0, 1, 2, 4, 7]

# 테스트 케이스 입력
for _ in range(t):
	val = int(input())

	# opt에 해당 값이 없으면 계산
	while len(opt) < val + 1:
		opt.append((opt[-1] + opt[-2] + opt[-3]) % 1000000009)

	# 출력
	print(opt[val])