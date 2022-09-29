'''
opt(i, j) := 문자열A의 i번문자와 문자열B의 j번문자의 LCS 길이
opt(i, j) = 
	opt(i-1, j-1) + 1  (A[i] == B[j]일 때 LCS에 추가할 수 있음)
	max(opt(i-1, j), opt(i, j-1))   (A[i] != B[j]일 때 LCS에 추가하지 못함)

이거 베이스에 역추적 기능도 있어야 함
역추적에는 '내가 어디서 왔는지' '나는 LCS에 포함되는지'를 기억해서 역추적
'''
import sys
input = sys.stdin.readline

# input
A = input().rstrip()
B = input().rstrip()

# process
# dp
opt = [[0 for _ in range(len(B))] for _ in range(len(A))]
prev = [[None for _ in range(len(B))] for _ in range(len(A))]

for i in range(len(A)):
	for j in range(len(B)):

		if A[i] == B[j]:
			opt[i][j] = opt[i - 1][j - 1] + 1 if i > 0 and j > 0 else 1
			prev[i][j] = (i - 1, j - 1, True)

		else:
			val1 = opt[i - 1][j] if i > 0 else 0
			val2 = opt[i][j - 1] if j > 0 else 0
			
			if val1 > val2:
				opt[i][j] = val1
				prev[i][j] = (i - 1, j, False)
			else:
				opt[i][j] = val2
				prev[i][j] = (i, j - 1, False)

# 역추적
LCS = []

i = len(A) - 1
j = len(B) - 1

while i >= 0 and j >= 0:
	i_prev, j_prev, isLCS = prev[i][j]
	if isLCS:
		LCS.append(A[i])
	i = i_prev
	j = j_prev

LCS.reverse()

# output
print(opt[len(A) - 1][len(B) - 1])
if opt[len(A) - 1][len(B) - 1] > 0:
	print(''.join(LCS))