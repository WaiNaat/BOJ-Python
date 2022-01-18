### 틀렸습니다 ###
'''
반례:
4 2
4594
'''
import heapq
# input
n, k = map(int, input().split())
num = list(input())
# process
'''
작은 숫자부터 k개를 지우되
같은 숫자가 여러 개일 경우 앞에서 지운다.
빨리 지우기 위해 최소 힙을 사용
	우선순위: 숫자, 그 숫자의 위치
다 지웠으면 남은 숫자들을 위치 오름차순으로 정렬함.
'''
num = list(zip(num, [i for i in range(n)]))
heapq.heapify(num)
for _ in range(k):
	heapq.heappop(num)
num.sort(key = lambda x: x[1])
sol = []
for val, _ in num:
	sol.append(val)
# output
print("".join(sol))