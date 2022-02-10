# input
n = int(input())
box = tuple(map(int, input().split()))
# process
'''
증가하는 부분 수열의 최대 길이를 구하는 문제.
i번째 상자에 대해 본인을 가장 큰 상자로 하는 최대 상자 개수를 opt(i)라 하면
opt(i) = max(opt(j) + 1, 1) (0<=j<i, box(j)<box(i))
'''
opt = [1 for _ in range(n)]

for i in range(1, n):
	for j in range(i):
		if box[j] < box[i] and opt[i] < opt[j] + 1:
			opt[i] = opt[j] + 1
# output
print(max(opt))