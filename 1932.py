import sys
input = sys.stdin.readline
# input & process
'''
i번째 줄의 j번째 숫자를 number(i, j),
number(i, j)를 마지막으로 하는 최대 합 경로를 opt(i, j)라 하면
opt(i, j) = max(opt(i-1, j-1), opt(i-1, j)) + number(i, j)

정답은 max(opt(n, j)) (0<=j<n)

prev := 삼각형의 i-1번째 줄
cur := 삼각형의 i번째 줄
'''
n = int(input())
prev = [int(input()), -1]
for i in range(1, n):
	cur = list(map(int, input().split()))
	for j in range(len(cur)):
		cur[j] += max(prev[j - 1], prev[j])
	prev = cur
	prev.append(-1)
# output
print(max(prev))