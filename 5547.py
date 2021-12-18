import sys
input = sys.stdin.readline

# functinos
# (w,h) 주변의 육각형 좌표 return
def adjCoords(w, h):
	if h % 2 == 0: # h가 짝수
		return [[w, h-1], [w+1, h-1], 
				[w-1, h], [w+1, h], 
				[w, h+1], [w+1, h+1]]
	else: # h가 홀수
		return [[w-1, h-1], [w, h-1], 
				[w-1, h],   [w+1, h],
				[w-1, h+1], [w, h+1]]

def DFS(w, h, width, height):
	stack = []
	isInside = True
	wall = 0

	home[h][w] = -1
	stack.append((w, h))

	while stack:
		w, h = stack.pop()
		for w2, h2 in adjCoords(w, h):
			# 지도 밖과 맞닿아 있으면 집으로 둘러싸이지 않았단 뜻
			if not 0 <= w2 < width or not 0 <= h2 < height:
				isInside = False
			# 집과 맞닿아 있으면 칠함
			elif home[h2][w2] == 1:
				wall += 1
			# 집이 없는 부분을 탐색
			elif home[h2][w2] == 0:
				home[h2][w2] = -1
				stack.append((w2, h2))

	return isInside, wall

# input
width, height = map(int, input().split())
home = [list(map(int, input().split())) for _ in range(height)]

# process
'''
1. DFS로 건물이 없는 곳이 집으로 둘러싸였는지 아니면 밖에서 보이는지 알 수 있음
	건물이 없는 곳이고 집으로 둘러싸이지 않았을 경우 집과 닿는 부분을 칠함
2. 지도 테두리에 집이 있는지 확인
	지도 테두리의 집은 지도 바깥쪽과 닿는 부분을 칠함
'''
cnt = 0
for h in range(height):
	for w in range(width):
		# 건물이 아닌 공간을 탐색
		if home[h][w] == 0:
			isInside, wall = DFS(w, h, width, height)
			if not isInside:
				cnt += wall
		# 지도 테두리의 건물
		elif home[h][w] == 1:
			if w == 0 or w == width - 1 or h == 0 or h == height - 1:
				for w2, h2 in adjCoords(w, h):
					if not 0 <= w2 < width or not 0 <= h2 < height:
						cnt += 1

# output
print(cnt)