'''
막줄에 누가누가 있느냐가 중요함
opt(i) := 막줄을 i번부터 시작할 때 최소 남는칸의제곱의합
rest(i, j) := i번부터 j번 이름을 막줄에 적을 수 있을 때 남는칸의제곱의합
opt(i) =
	opt(k) + rest(k, i-1)^2
	이 값들 중 최솟값

정답은 min(opt(x))
	x는 rest(x, N)>=0 인 x
'''
import sys
input = sys.stdin.readline

# input
N, length = map(int, input().split())
name = [int(input()) for _ in range(N)]

# process
opt = [float('inf') for _ in range(N)]
opt[0] = 0

for i in range(N):
	rest = length + 1
	for k in range(i - 1, -1, -1):
		rest -= 1 + name[k]
		if rest < 0: break
		opt[i] = min(opt[k] + rest ** 2, opt[i])

sol = float('inf')
rest = length + 1
for x in range(N - 1, -1, -1):
	rest -= 1 + name[x]
	if rest < 0: break
	sol = min(opt[x], sol)

# output
print(sol)