import sys
input = sys.stdin.readline
import heapq
# input
n, m, k = map(int, input().split())
beer = [tuple(map(int, input().split())) for _ in range(k)]
# process
'''
일단 도수 낮은거부터 n병 마신다.
선호도 합을 못 채웠으면 선호도 제일 낮은 거 빼고
다음 도수 낮은걸 마신다.

beer := 도수 레벨 오름차순으로 정렬한 배열. (선호도, 도수)
drink := 마실 맥주들. 선호도 낮은 게 우선인 힙.
'''
beer.sort(key=lambda x: x[1])

drink = []
liver = 0
satisfaction = 0
satisfied = False

for b in beer:
	# n병 못 채웠으면 마신다.
	if len(drink) < n:
		heapq.heappush(drink, b)
		satisfaction += b[0]
		liver = max(liver, b[1])
	# n병은 채웠는데 만족하지 못한 경우.
	elif satisfaction < m:
		v, _ = heapq.heapreplace(drink, b)
		satisfaction += b[0] - v
		liver = max(liver, b[1])
	# n병도 채우고 만족한 경우
	if satisfaction >= m and len(drink) == n:
		satisfied = True
		break
# output
print(liver) if satisfied else print(-1)