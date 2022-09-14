'''
일단 학생의 선택지는 1. 현재 조에 들기 2. 내가 새로운 조가 되기
이러면 현재 조가 어디부터 어디인지까지를 알아야 함

opt(i) := i명의 학생들로 조를 짰을 때 잘짜정의 최댓값
group(i, j) := 조의 구성원이 i~j번 학생일 때 잘짜정
opt(i) = max(opt(j) + group(j + 1, i))
		단, -1 <= j < i, opt(-1)=0
'''
import sys
input = sys.stdin.readline

# input
N = int(input())
score = tuple(map(int, input().split()))

# process
opt = [0 for _ in range(N)]

for i in range(1, N):
	
	max_score = -1
	min_score = 12345

	for j in range(i - 1, -2, -1):
		
		max_score = max(score[j + 1], max_score)
		min_score = min(score[j + 1], min_score)
		group = max_score - min_score

		opt[i] = max((opt[j] if j >= 0 else 0) + group, opt[i])

# output
print(opt[N - 1])