import sys, heapq
input = sys.stdin.readline
# input
n = int(input())
army_tiger = [tuple(map(int, input().split())) for _ in range(n)]
# process
'''
싸지방 이용 시작 시간 오름차순 정렬.
정렬된 앞사람부터 싸지방 쓰는데
빈 자리가 없으면 새로운 컴퓨터 구매.

만약 빈 자리가 여러 개면 앞쪽 자리부터 채워야 함.
>> 자기가 사용할 수 있는 자리들을 모두 힙에서 pop한 다음
	그 중에서 제일 앞쪽 자리 사용.

pc_num := 현재까지 만들어진 pc 번호.
pc_end := 컴퓨터 끝나는 시간 최소 힙.
pc_cnt := 각 pc 번호마다 이용한 사람 수 배열.
pc_available := 현재 사용 가능한 pc 번호.
'''
army_tiger.sort()

pc_num = -1
pc_end = []
pc_cnt = []
pc_available = []
for start, end in army_tiger:
	# 현재 사용할 수 있는 자리들 업데이트
	while pc_end and pc_end[0][0] < start:
		_, num = heapq.heappop(pc_end)
		heapq.heappush(pc_available, num)
	# 사용할 수 있는 자리가 있으면 거기 사용
	if pc_available:
		pc = heapq.heappop(pc_available)
		heapq.heappush(pc_end, (end, pc))
		pc_cnt[pc] += 1
	# 새로운 pc 구매
	else:
		pc_num += 1
		heapq.heappush(pc_end, (end, pc_num))
		pc_cnt.append(1)
# output
print(len(pc_cnt))
print(*pc_cnt)