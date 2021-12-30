import sys
input = sys.stdin.readline
from collections import deque

# input
sm_speed, js_speed, n = map(int, input().split())
sm_available = js_available = 1
sm_work = deque([])
js_work = deque([])
for _ in range(n):
	t, c, m = input().split()
# process
	'''
	상민이가 현재 일을 할 수 있는지, 지수가 현재 일을 할 수 있는지에 따라
	들어오는 일들의 시작시간을 정한다.

	나중에 시작시간을 비교해서 선물 번호를 붙인다.
	시작시간이 같은 경우 상민이 선물 번호가 앞선다.
	'''
	t = int(t)
	m = int(m)
	if c == 'B':
		for _ in range(m):
			start = sm_available if sm_available > t else t
			sm_available = start + sm_speed
			sm_work.append(start)
	else:
		for _ in range(m):
			start = js_available if js_available > t else t
			js_available = start + js_speed
			js_work.append(start)

# merge sort 합치는 것과 같은 원리로 번호 부여.
sm_done = []
js_done = []
giftNo = 1
while sm_work and js_work:
	sm_cur = sm_work[0]
	js_cur = js_work[0]
	if sm_cur <= js_cur:
		sm_done.append(giftNo)
		sm_work.popleft()
	else:
		js_done.append(giftNo)
		js_work.popleft()
	giftNo += 1

if sm_work:
	for _ in range(len(sm_work)):
		sm_done.append(giftNo)
		giftNo += 1
if js_work:
	for _ in range(len(js_work)):
		js_done.append(giftNo)
		giftNo += 1

# output
print(len(sm_done))
print(*sm_done)
print(len(js_done))
print(*js_done)