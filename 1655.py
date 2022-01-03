import heapq
import sys
input = sys.stdin.readline
# input
n = int(input())
left = []
right = []
for i in range(n):
	num = int(input())
# process
	'''
	백준이 말한 수들의 배열은 중간값을 기준으로
		왼쪽 힙: 최대 힙 << 값들에 다 -1 곱해서 넣어야 함.
		오른쪽 힙: 최소 힙
	의 두 개 힙으로 나눌 수 있다.
	이때 홀수번 말했으면 왼쪽 힙의 뿌리가,
	짝수번 말했으면 두 힙의 뿌리 중 작은 값이 중간값. 
		>> 근데 어차피 왼쪽 힙 뿌리 <= 오른쪽 힙 뿌리임.
	>> 왼쪽 힙과 오른쪽 힙의 크기는 같거나 왼쪽이 1 더 커야 함.

	백준이 새로운 숫자 num을 말했을 때
	num <= 왼쪽 힙의 뿌리면: 왼쪽 힙에 넣어야 함.
	아니면: 오른쪽 힙에 넣어야 함.
	이후 힙 크기의 균형이 깨졌으면
		크기가 큰 쪽에서 pop해서 작은 쪽에 push해서 균형을 맞춰 줌.
	'''
	if i == 0 or num <= -left[0]: heapq.heappush(left, -num)
	else: heapq.heappush(right, num)

	if len(left) > len(right) + 1:
		heapq.heappush(right, -heapq.heappop(left))
	elif len(right) > len(left):
		heapq.heappush(left, -heapq.heappop(right))
# output
	print(-left[0])