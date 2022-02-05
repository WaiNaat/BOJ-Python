import sys
input = sys.stdin.readline
# input
row, col = map(int, input().split())
campus = [list(input().rstrip()) for _ in range(row)]
# process
# 도연 씨 위치 찾기
x = y = 0
found = False
for i in range(row):
	if found: break
	for j in range(col):
		if campus[i][j] == 'I':
			x = j
			y = i
			found = True
# dfs
cnt = 0
stack = [(x, y)]
moves = ((0, 1), (1, 0), (0, -1), (-1, 0))
campus[y][x] = 'X'
while stack:
	x, y = stack.pop()
	for dx, dy in moves:
		x2 = x + dx
		y2 = y + dy
		if not 0 <= x2 < col or not 0 <= y2 < row:
			continue
		if campus[y2][x2] == 'X':
			continue
		if campus[y2][x2] == 'P':
			cnt += 1
		stack.append((x2, y2))
		campus[y2][x2] = 'X'
# output
print(cnt if cnt > 0 else "TT")