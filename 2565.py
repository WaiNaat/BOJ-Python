import sys
input = sys.stdin.readline

# input
n = int(input())
wire = [tuple(map(int, input().split())) for _ in range(n)]

# process
'''
(A, B)쌍을 A 기준 오름차순 정렬,
B 전봇대의 위치들을 수열이라 치고
DP로 그 수열에서 감소하지 않는 부분 수열의 최대 길이를 구하는 문제!

위의 '그 수열'을 B라 하고
opt(i)를 B[0]~B[i]에서 B[i]를 마지막으로 하고 감소하지 않는 부분수열의 최대 길이라 하면
opt(i) = 
	1
	opt(j) + 1  (j는 j<i, B[j] < B[i]인 j들 중 opt(j)가 최대인 j)
둘 중 큰 값
'''
wire.sort()

opt = [0 for _ in range(n)]

for i in range(n):
	for j in range(i):
		if wire[j][1] < wire[i][1] and opt[i] < opt[j]:
			opt[i] = opt[j]
	opt[i] += 1

# output
print(n - max(opt))