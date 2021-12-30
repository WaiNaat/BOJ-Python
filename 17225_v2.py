### 틀렸습니다 ###

import sys
input = sys.stdin.readline
from collections import deque
# class
class PartTime:
	'''
	giftNo := 선물 번호
	'''
	giftNo = 1

	def __init__(self):
		'''
		work_done := 완료한 선물 번호 목록.
		work := 선물들의 포장 시작 시간.
		speed := 포장하는 데 걸리는 시간.
		available := 이 시간 이전에는 포장 하는 중.
		'''
		self.work_done = []
		self.work = deque([])
		self.speed = -1
		self.cur = None
		self.available = 0
	
	def do_work(self, time):
		'''
		선물 포장을 시작해야 하는 경우 포장 시작함.
		'''
		while self.work and self.work[0] == time:
			self.work_done.append(PartTime.giftNo)
			self.work.popleft()
			PartTime.giftNo += 1

	def isWorking(self):
		'''
		일이 끝났으면 False, 아직 할 일이 남았으면 True
		'''
		return True if self.work else False

	def add_work(self, order, number):
		'''
		주문시각 order에 이미 포장중인 게 있으면 avilable한 시간부터 포장 시작
		아니면 order 시간부터 즉시 포장 시작
		'''
		for _ in range(number):
			start = self.available if self.available > order else order
			end = start + self.speed
			self.work.append(start)
			self.available = end

# input
sangmin = PartTime()
jisoo = PartTime()
sangmin.speed, jisoo.speed, n = map(int, input().split())
for _ in range(n):
	t, c, m = input().split()
	if c == 'B': sangmin.add_work(int(t), int(m))
	else: jisoo.add_work(int(t), int(m))
# process
'''
두 개의 큐를 이용해서 상민이와 지수의 일을 처리한다.
	>> input 과정에서 색깔별로 일을 분류.
두 사람이 동시에 선물 포장을 시작할 경우 상민이 번호가 앞섬
	>> 코드 순서로 쉽게 적용 가능.
'''
time = 0
while sangmin.isWorking() or jisoo.isWorking():
	time += 1
	sangmin.do_work(time)
	jisoo.do_work(time)
# output
print(len(sangmin.work_done))
print(*sangmin.work_done)
print(len(jisoo.work_done))
print(*jisoo.work_done)