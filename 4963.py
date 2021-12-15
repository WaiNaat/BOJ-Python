import sys
input = sys.stdin.readline

# functions
def countIsland(width, height):
	cnt = 0
	for h in range(height):
		for w in range(width):
			if M[h][w] == 1: # 방문하지 않은 섬 군집 발견시 방문
				DFS(w, h, width, height)
				cnt += 1
	return cnt

def DFS(w, h, width, height):
	stack = [] # 스택을 이용한 DFS
	moveX = (1, 0, -1)
	moveY = (1, 0, -1)

	M[h][w] = -1 # 방문한 섬은 -1로 표시함.
	stack.append((w, h))

	while stack:
		w, h = stack.pop()
		for dx in moveX:
			for dy in moveY:
				w2 = w + dx
				h2 = h + dy
				if not 0 <= h2 < height or not 0 <= w2 < width:
					continue
				if M[h2][w2] == 1:
					M[h2][w2] = -1
					stack.append((w2, h2))

# input
while True:
	width, height = map(int, input().split())
	if width == 0: break
	M = [list(map(int, input().split())) for _ in range(height)]
# process & output
	print(countIsland(width, height))