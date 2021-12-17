import sys
input = sys.stdin.readline

# function
def DFS(w, width, height):
	stack = []
	move = ((0, 1), (0, -1), (1, 0), (-1, 0))

	textile[0][w] = -1
	stack.append((w, 0))

	while stack:
		w, h = stack.pop()
		for dx, dy in move:
			w2 = w + dx
			h2 = h + dy
			if not 0 <= w2 < width or not 0 <= h2 < height:
				continue
			if textile[h2][w2] == 0:
				if h2 == height - 1: # 안쪽 격자에 도착
					return True
				textile[h2][w2] = -1
				stack.append((w2, h2))
	return False

# input
height, width = map(int, input().split())
textile = [list(map(int, list(input().rstrip()))) for _ in range(height)]
# process
canPercolate = False
# 바깥쪽 격자들에 전류를 흘려준다.
for w in range(width):
	if textile[0][w] == 0:
		canPercolate = DFS(w, width, height)
		if canPercolate: break
# output
print("YES") if canPercolate else print("NO")