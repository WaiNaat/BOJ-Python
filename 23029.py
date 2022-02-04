import sys
input = sys.stdin.readline
# input
n = int(input())
food = [int(input()) for _ in range(n)]
# process
'''
i번 시식코너의 음식 개수를 food(i),
0번~i번 시식코너에서 아리가 먹은 음식의 최대 개수를 opt(i)라 하면
opt(i) =
	opt(i-1)  (i번 시식 안 함)
	food(i)/2 + food(i-1) + opt(i-3)  (i-2번 시식 안 함)
	food(i) + opt(i-2)  (i-1번 시식 안 함)
	셋 중 큰 값.
'''
opt = [0 for _ in range(max(3, n))]
if len(food) < 3:
	food.append(0)
	food.append(0)
opt[0] = food[0]
opt[1] = food[0] + food[1] // 2
opt[2] = max(opt[1], food[0] + food[2], food[1] + food[2] // 2)

for i in range(3, n):
	opt[i] = max(
		opt[i - 1],
		food[i] // 2 + food[i - 1] + opt[i - 3],
		food[i] + opt[i - 2]
	)
# output
print(max(opt))