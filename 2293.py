###  시간 초과  ###

import sys
input = sys.stdin.readline

'''
coin(i)를 i번째 동전의 가치,
opt(i, j)를 i개의 동전을 써서 j원을 만드는 경우의 수라 하면
opt(i, j) = 
	sum( opt(i-1, j-coin(i)*x),   (x는 0 이상의 정수)
		 1   (coin(i)만으로 j를 만들 수 있을 때)
	)

prev := opt(i-1, ?)를 나타내는 배열
cur := opt(i, ?)를 나타내는 배열
'''

# n과 k 입력
n, k = map(int, input().split())

# 초기화
prev = [0 for _ in range(k + 1)]

# 동전 입력
for _ in range(n):
	coin = int(input())
	cur = [0 for _ in range(k + 1)]

	# 방금 입력된 동전만으로 j원을 만들 수 있을 경우
	for j in range(coin, k + 1, coin):
		cur[j] = 1

	# i-1개의 동전에 i번 동전을 더해 j원을 만들 수 있을 경우
	for j in range(k + 1):
		for x in range(j // coin + 1):
			cur[j] += prev[j - coin * x]

	prev = cur

# 출력
print(prev[k])