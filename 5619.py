import sys, heapq
input = sys.stdin.readline
from itertools import permutations
# input
h = []
n = int(input())
for _ in range(n):
	val = int(input())
	if len(h) < 4:
		heapq.heappush(h, -val)
	elif val < -h[0]:
		heapq.heapreplace(h, -val)
# process
'''
가장 작은 수 4개를 봐야 함.
네 개의 수 중 하나는 가장 작은 수를 만들 때 맨 앞에 들어감.
그럼 나머지 3개를 이용해서 세 개의 수를 만들 수 있음.

근데 네 개의 수 중 뭐가 앞쪽에 들어가는지 모르기 때문에
완전탐색 사용 >> 4P2 = 12라 금방 함.
'''
h = map(lambda x: -x, h)
p = permutations(h, 2)

nums = []
for a, b in p:
	nums.append(int("".join( (str(a), str(b)) )))

nums = list(map(int, nums))
nums.sort()
# output
print(nums[2])