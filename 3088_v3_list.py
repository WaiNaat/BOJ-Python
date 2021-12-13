import sys
input = sys.stdin.readline

# input
N = int(input())
num = [0 for _ in range(1000001)]
sol = 0
for i in range(N):
	a, b, c = map(int, input().split())
# process
	'''
	num[i] := 이전까지 깨진 화분에 i가 적혀 있었으면 1, 아니면 0

	i번째 화분에 대해
		이전에 깨진 화분들의 숫자와 하나라도 같은 게 있으면 얘도 깨짐.
		아니면 직접 깨야 함.
	'''
	if num[a] == 0 and num[b] == 0 and num[c] == 0:
		sol += 1
	num[a] = num[b] = num[c] = 1
# output
print(sol)