### 틀렸습니다 ###

import sys, heapq
input = sys.stdin.readline
# input
n = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(n)]
# process
'''
'회의실 배정'의 탈락자들을 다시 배정하는 문제.
끝나는 시간 오름차순 정렬.
만약 다음 강의의 시작시간이 현재 강의실들의 종료시간보다 빠르면
	새로운 강의실에 배정.
아니면 현재 강의실 중 가장 종료 시간이 빠른 강의실에 배정함.
	>> 강의실별 종료시간을 저장하는 최소 힙 필요.

sol := 각 강의가 몇 번 강의실인지 저장하는 배열.
classrooms := 각 강의실의 종료시간을 저장하는 최소 힙.
'''
k = 1
sol = [None for _ in range(n + 1)]
classrooms = [(-1, 1)]

lectures.sort(key = lambda x: (x[2], x[1]))

for lecture_no, start, end in lectures:
	classroom_end, classroom_no = classrooms[0]
	if start >= classroom_end:
		heapq.heapreplace(classrooms, (end, classroom_no))
	else:
		k += 1
		classroom_no = k
		heapq.heappush(classrooms, (end, k))
	sol[lecture_no] = classroom_no
# output
print(k)
for i in range(1, n + 1): print(sol[i])