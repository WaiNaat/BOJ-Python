import sys
input = sys.stdin.readline

# input
T = int(input())
for _ in range(T):
	N = int(input())
	log = list(map(int, input().split()))
# process
	'''
	통나무를 오름차순으로 정렬.
	0번 통나무를 기준으로 양 방향으로 뻗어나가는 모양으로 통나무를 배치.
		0번 통나무 양 옆에 통나무를 세운다고 생각했을 때,
			1번 통나무와 2번 통나무를 각각 왼쪽과 오른쪽에 세우면 높이차가 최소가 된다.
		1번 통나무 왼쪽에는 3번 통나무를 세워야 높이차가 최소가 된다.
		2번 통나무 오른쪽에는 4번 통나무를 세워야 높이차가 최소가 된다.
		...
	양 끝을 연결하면 완성.
	'''
	log.sort()

	left = right = log[0]
	max_diff = 0
	isLeft = True
	for i in range(1, N):
		val = log[i]
		diff = 0
		if isLeft:
			diff = val - left
			left = val
		else:
			diff = val - right
			right = val
		if diff > max_diff: max_diff = diff
		isLeft = not isLeft
	max_diff = max(max_diff, abs(left - right))
# output
	print(max_diff)