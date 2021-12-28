import sys
input = sys.stdin.readline
# functions
def cut(value):
	'''
	value 길이로 랜선을 자를 때 나오는 개수
	'''
	cnt = 0
	for i in lan: cnt += i // value
	return cnt

# input
K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]
# process
'''
x 길이로 모든 랜선을 자른다고 할 때
만든 랜선 개수 < N 이면 x를 줄여야 함.
반대면 x를 늘려봐야 함.
'''
left = 1
right = max(lan) + 1
while left < right:
	mid = (left + right) // 2
	if cut(mid) < N: right = mid
	else: left = mid + 1
# output
print(left - 1)