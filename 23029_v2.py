import sys
input = sys.stdin.readline
# input
n = int(input())
food = [int(input()) for _ in range(n)]
# process
'''
i번 시식코너의 음식 개수를 food(i),
opt(i, prev, prev2)를 i번째 시식코너에서 최대로 먹을 수 있는 음식의 양인데
prev, prev2는 각각 i-1, i-2번째 시식코너에서 음식을 먹었는지의 여부라 하면
opt(i, 1, 0) =
	food(i)/2 + max(opt(i-1, 0, 1), opt(i-1, 0, 0))
opt(i, 0, 1) =
	food(i) + max(opt(i-2, prev, prev2))
opt(i, 0, 0) =
	food(i) + max(opt(i-3, prev, prev2))
'''
opt = [ [[0, 0], [0, 0]] for _ in range(n + 3)]
opt[0][0][0] = food[0]

sol = food[0]
for i in range(1, n):
	opt[i][1][0] = food[i] // 2 + max(opt[i - 1][0][1], opt[i - 1][0][0])
	opt[i][0][1] = food[i] + max(opt[i - 2][0][0], opt[i - 2][1][0], opt[i - 2][0][1])
	opt[i][0][0] = food[i] + max(opt[i - 3][0][0], opt[i - 3][1][0], opt[i - 3][0][1])
	sol = max(opt[i][1][0], opt[i][0][1], opt[i][0][0], sol)
# output
print(sol)