### 틀렸습니다 ###

import sys
input = sys.stdin.readline
from collections import deque
# class
class PartTime:
	'''
	work_done := 완료한 선물 번호 목록
	work := 할 일들
	speed := 포장하는 데 걸리는 시간
	cur := 현재 포장중인 선물의 진행상황 [0]번호, [1]진행시간 [2]완성시간
	'''
	def __init__(self):
		self.work_done = []
		self.work = deque([])
		self.speed = -1
		self.cur = None
	
	def do_work(self, time, giftNo):
		'''
		input : 현재시각, 새로운 선물 번호
		return : 이번 단위시간동안 포장한 선물 개수
		'''
		# 포장 작업 진행
		if self.cur is not None:
			self.cur[1] += 1
			if self.cur[1] == self.cur[2]:
				self.work_done.append(self.cur[0])
				self.cur = None
		# 진행중인 작업 없으면 새 일 시작
		if self.cur is None and self.work and self.work[0] <= time:
			# 포장속도가 0이면 단위시간동안 여러개 할 수도 있음.
			if self.speed == 0: 
				cnt = 0
				while self.work and self.work[0] <= time:
					self.work.popleft()
					self.work_done.append(giftNo)
					giftNo += 1
					cnt += 1
				return cnt

			self.cur = [giftNo, 0, self.speed]
			self.work.popleft()
			return 1
		return 0
	
	def isWorking(self):
		if self.work or self.cur is not None: return True
		else: return False

	def add_work(self, time, number):
		for _ in range(number): self.work.append(time)

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
giftNo = 1
while sangmin.isWorking() or jisoo.isWorking():
	time += 1
	giftNo += sangmin.do_work(time, giftNo)
	giftNo += jisoo.do_work(time, giftNo)
# output
print(len(sangmin.work_done))
print(*sangmin.work_done)
print(len(jisoo.work_done))
print(*jisoo.work_done)