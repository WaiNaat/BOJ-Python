import sys, heapq
input = sys.stdin.readline
# input
n = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(n)]
# process
'''
수업들을 시작 시간 오름차순으로 정렬.
현재 사용중인 강의실들의 끝나는 시간 최소 힙.
수업들을 앞에서부터 하나씩 살펴보는데
	이 수업이 현재 위에서 말한 힙의 뿌리 강의실에서 가능하면
	거기서 진행하고
	아니면 새로운 강의실에서 진행.
'''
lectures.sort()
h = []
cnt = 0
for start, end in lectures:
	if h and h[0] <= start:
		heapq.heapreplace(h, end)
	else:
		heapq.heappush(h, end)
		cnt += 1
# output
print(cnt)