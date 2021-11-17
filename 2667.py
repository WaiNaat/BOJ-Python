# functions
def getEstate(N):
	sol = []
	visited = [[0 for _ in range(N+2)] for _ in range(N+2)]

	for row in range(1, N+1):
		for col in range(1, N+1):
			global cnt
			cnt = 0 # number of houses in one estate
			if G[row][col] == '1' and visited[row][col] == 0:
				DFS((row, col), visited)
				sol.append(cnt)
	return sol

# one call of DFS() can find one housing estate
def DFS(v, visited):
	global cnt
	# visit current vertex
	r, c = v
	visited[r][c] = 1
	cnt += 1
	# move right
	if G[r][c+1] == '1' and visited[r][c+1] == 0:
		DFS((r,c+1), visited)
	# move down
	if G[r+1][c] == '1' and visited[r+1][c] == 0:
		DFS((r+1, c), visited)
	# move up
	if G[r-1][c] == '1' and visited[r-1][c] == 0:
		DFS((r-1, c), visited)
	# move left
	if G[r][c-1] == '1' and visited[r][c-1] == 0:
		DFS((r, c-1), visited)


# input
N = int(input())
G = ["" for _ in range(N+2)]
# zero padding
pad = ['0' for _ in range(N+2)]
pad = ''.join(pad)
G[0] = pad
G[N+1] = pad
# get input
for i in range(1, N+1):
	G[i] = ''.join(['0', input(), '0'])

# process
sol = getEstate(N)
sol.sort()

# output
print(len(sol))
for i in sol: print(i)