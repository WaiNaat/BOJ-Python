'''
틀렸습니다

반례
3
1 2 3
2
'''

# input
N = int(input())
A = list(map(int, input().split()))
S = int(input())

# process
for i in range(S):
	changed = False
	# 두 개를 바꿨을 때 사전 순으로 뒷서면 교환
	for j in range(N-1):
		if A[j] < A[j + 1]:
			A[j], A[j+1] = A[j+1], A[j]
			changed = True
			break
	# 더 이상 바꿀 게 없으면 종료
	if not changed: break

# output
for i in A: print(i, end=' ')