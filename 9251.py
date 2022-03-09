# input
A = input()
B = input()

# process
'''
https://ko.wikipedia.org/wiki/최장_공통_부분_수열

opt(i, j)를 두 문자열 A[0]~A[i], B[0]~B[j]의 LCS의 길이라 하면
opt(i, j) = 
	opt(i-1, j-1) + 1   (A[i]=B[j]일 때)
	max( opt(i-1, j), opt(i, j-1) )   (A[i]!=B[j]일 때)

opt는 이차원 배열로 나타낼 수 있지만
opt(i, j)를 계산하는 데는 opt(?, j-1)만 보면 되므로
prev, cur의 두 배열을 이용해 각각 opt(?, j-1), opt(?, j)를 나타낸다.
'''
prev = [0 for _ in range(len(A))]

for j in range(len(B)):
	cur = [1 if A[0] == B[j] else prev[0]]

	for i in range(1, len(A)):
		if A[i] == B[j]:
			cur.append(prev[i - 1] + 1)
		else:
			cur.append(max(cur[i - 1], prev[i]))
	
	prev = cur

# output
print(prev[-1])