### 시간 초과 ###

import sys
input = sys.stdin.readline
# input
n = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(n)]
# process
'''
'회의실 배정'의 탈락자들을 다시 배정하는 문제.
끝나는 시간 오름차순 정렬.
일단 회의실 배정을 하고, 탈락자들을 모아 다시 반복.

sol := 각 강의가 몇 번 강의실인지 저장하는 배열.
'''
k = 0
sol = [None for _ in range(n + 1)]

lectures.sort(key = lambda x: (x[2], x[1], x[0]))

while lectures:
	k += 1
	aux = []
	classroom_end = -1
	for lecture in lectures:
		lecture_no, start, end = lecture
		if start >= classroom_end:
			classroom_end = end
			sol[lecture_no] = k
		else:
			aux.append(lecture)
	lectures = aux

# output
print(k)
for i in range(1, n + 1): print(sol[i])