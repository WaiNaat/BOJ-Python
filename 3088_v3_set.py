import sys
input = sys.stdin.readline

# input
N = int(input())
num = set([])
sol = 0
for i in range(N):
	pot = set(map(int, input().split()))
# process
	'''
	num := 이전에 깨진 화분들에 적힌 숫자들의 집합
	pot := 지금 들어온 화분에 적힌 숫자

	i번째 화분에 대해
		이전에 깨진 화분들의 숫자와 하나라도 같은 게 있으면 얘도 깨짐.
		아니면 직접 깨야 함.
	'''
	if not num & pot:
		sol += 1	
	num |= pot

# output
print(sol)