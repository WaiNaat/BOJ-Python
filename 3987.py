import sys
input = sys.stdin.readline
# class
class Signal:
	def __init__(self, x, y, dir):
		self.x = x
		self.y = y
		self.dir = dir
		self.time = 1
		self.canMove = True
		self.isLoop = False
		self.moved = set()
		self.initial_dir = dir
	
	def move(self):
		'''
		현재 방향에 따라 움직임.
		'''
		if not self.canMove or self.isLoop: return
		if self.dir == 'U': self.y -= 1
		elif self.dir == 'D': self.y += 1
		elif self.dir == 'L': self.x -= 1
		else: self.x += 1
		self.time += 1
	
	def updateState(self, planet):
		'''
		현재 위치의 상태에 따라 시그널의 상태 변화.
		'''
		if not self.canMove or self.isLoop: return
		# 항성계 밖
		if planet is False:
			self.time -= 1
			self.canMove = False
			return
		# 블랙홀
		elif planet == 'C':
			self.time -= 1
			self.canMove = False
			return
		# 행성 발견시 방향 전환
		elif planet == '/':
			if self.dir == 'U': self.dir = 'R'
			elif self.dir == 'D': self.dir = 'L'
			elif self.dir == 'L': self.dir = 'D'
			else: self.dir = 'U'
		elif planet == '\\': # \
			if self.dir == 'U': self.dir = 'L'
			elif self.dir == 'D': self.dir = 'R'
			elif self.dir == 'L': self.dir = 'U'
			else: self.dir = 'D'
		# 루프인지 확인
		if (self.x, self.y, self.dir) in self.moved:
			self.isLoop = True
		else:
			self.moved.add((self.x, self.y, self.dir))

	def outOfSpace(self, xmax, ymax):
		'''
		우주의 범위를 입력했을 때 우주 밖인지 알려주는 함수.
		'''
		return False if 0 <= self.x < xmax and 0 <= self.y < ymax else True
		
# input
ymax, xmax = map(int, input().split())
space = [input().rstrip() for _ in range(ymax)]
yPos, xPos = map(int, input().split())
# process
'''
상하좌우로 시그널을 보내야 함.
각 시그널별로 현재 위치, 이동 방향, 시간 저장.
각 시그널별로 위치-방향 쌍 저장.
	>> 한 시그널에서 이게 중복되면 무한루프.
'''
signals = [Signal(xPos - 1, yPos - 1, dir) for dir in ('U', 'R', 'D', 'L')]
isLoop = False
canMove = True

while not isLoop and canMove:
	canMove = False
	for signal in signals:
		signal.move()

		planet = None
		if signal.outOfSpace(xmax, ymax): planet = False
		else: planet = space[signal.y][signal.x]
		signal.updateState(planet)
		
		canMove = canMove or signal.canMove
		isLoop = isLoop or signal.isLoop

solDir = None
solTime = 0
if isLoop:
	for signal in signals:
		if signal.isLoop:
			solDir = signal.initial_dir
			solTime = "Voyager"
			break
else:
	for signal in signals:
		if signal.time > solTime:
			solDir = signal.initial_dir
			solTime = signal.time
# output
print(solDir)
print(solTime)


