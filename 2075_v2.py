import sys, heapq
input = sys.stdin.readline
# input & process
'''
n번째 큰 수 = 큰 수 n개 중에서 가장 작은 수
크기 n의 최소 힙 사용,
들어오는 입력값 x에 대해 x가 힙의 뿌리보다 크면
힙의 뿌리를 빼내고 x를 넣는다.
'''
n = int(input())
h = list(map(int, input().split()))
heapq.heapify(h)

for _ in range(1, n):
	line = map(int, input().split())
	for val in line:
		if val > h[0]:
			heapq.heapreplace(h, val)
# output
print(h[0])