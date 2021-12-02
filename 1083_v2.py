# input
N = int(input())
A = list(map(int, input().split()))
S = int(input())

# process
changeIdx = 0
while S > 0 and changeIdx < N:
	# A[changeIdx + 1]부터 A[changeIdx + S]까지의 값은 S번 이내의 교환으로 A[changeIdx]와 바꿀 수 있음
	# 그 값들 중 가장 큰 녀석과 바꾸면 사전순으로 가장 늦어짐
	maxIdx = -1
	maxVal = A[changeIdx]
	for j in range(changeIdx + 1, changeIdx + S + 1):
		if j >= N: break
		if maxVal < A[j]:
			maxVal = A[j]
			maxIdx = j
	if maxIdx != -1:
		for j in range(maxIdx, changeIdx, -1):
			A[j], A[j-1] = A[j-1], A[j]
		S -= maxIdx - changeIdx
	# 다음 숫자
	changeIdx += 1

# output
for i in A: print(i, end=' ')