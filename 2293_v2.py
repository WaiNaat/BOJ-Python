import sys
input = sys.stdin.readline

'''
coin(i)를 i번째 동전의 가치,
opt(i, j)를 0~i번 동전을 써서 j원을 만드는 경우의 수라 하면
opt(i, j) = 
	opt(i, j-coin(i))   (i번 동전을 사용하여 j원을 만드는 경우)
	+ opt(i-1, j)   (i번 동전을 사용하지 않고도 j원을 만드는 경우)

opt배열을 전부 만들 필요 없이
prev := opt(i-1, ?)를 나타내는 배열
cur := opt(i, ?)를 나타내는 배열
이거 두개만으로 가능.

opt(i, 0) = 1
	>> 아무것도 안하는 경우도 경우임.
'''

# n과 k 입력
n, k = map(int, input().split())

# 초기화
prev = [0 for _ in range(k + 1)]
prev[0] = 1

# 동전 입력
for _ in range(n):
	coin = int(input())

	# 점화식 계산
	cur = prev.copy()
	for j in range(k + 1):
		if j - coin >= 0:
			cur[j] += cur[j - coin]
	
	prev = cur

# 출력
print(prev[k])