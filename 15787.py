import sys
input = sys.stdin.readline
from collections import deque
# input
trainNum, command = map(int, input().split())
train = [deque(['0' for _ in range(20)]) for _ in range(trainNum)]
for _ in range(command):
	c = tuple(map(int, input().split()))
# process
	'''
	max(N)=max(M)=10만이므로 O(N+M) 알고리즘 가능.

	일단 명령들을 수행.
		3, 4명령은 기차를 deque으로 만들면 쉽게 처리 가능.
	그 다음에 출발 조건 확인.
	'''
	if c[0] == 1:
		train[c[1] - 1][c[2] - 1] = '1'
	elif c[0] == 2:
		train[c[1] - 1][c[2] - 1] = '0'
	elif c[0] == 3:
		train[c[1] - 1].rotate(1)
		train[c[1] - 1][0] = '0'
	else: # '4'
		train[c[1] - 1].rotate(-1)
		train[c[1] - 1][19] = '0'
	
cnt = 0
milky = set()
train = ["".join(t) for t in train]
for t in train:
	if t not in milky:
		milky.add(t)
		cnt += 1
# output
print(cnt)