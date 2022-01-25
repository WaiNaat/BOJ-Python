import sys
input = sys.stdin.readline
# input
n = int(input())
score = [int(input()) for _ in range(n)]
# process
'''
3연속 1계단은 ㄴㄴ >> 바로 이전 계단을 밟았으면 두 개 이전의 계단은 못 밟음.
n번째 계단 위에서의 총 점수를 opt(n)이라 하고
n번째 계단의 점수를 score(n)이라 하면
opt(n) =
	score(n) + score(n-1) + opt(n-3) (바로 이전 계단을 밟고 올 경우)
	score(n) + opt(n-2) (바로 이전 계단을 건너뛰어 올 경우)
	이 둘 중에 큰 값.
'''
opt = [0 for _ in range(n)]
opt[0] = score[0]
if n > 1:
	opt[1] = score[0] + score[1]
if n > 2:
	opt[2] = score[2] + max(score[1], score[0])

for i in range(3, n):
	opt[i] = score[i] + max(score[i - 1] + opt[i - 3], opt[i - 2])	
# output
print(opt[n - 1])