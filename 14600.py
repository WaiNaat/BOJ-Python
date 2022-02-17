# functions
def isComplete(row, col, size):
	'''
	주어진 사분면이 '완전'하면 True, 아니면 False
	'''
	for i in range(row, row + size):
		for j in range(col, col + size):
			if showerRoom[i][j] != 0:
				return False
	return True

def tile(row, col, size):
	global tile_num
	# base case
	if size == 2:
		tile_num += 1
		for i in range(row, row + size):
			for j in range(col, col + size):
				if showerRoom[i][j] == 0:
					showerRoom[i][j] = tile_num
		return
	# recursive step
	size //= 2
	# '완전한' 사분면 세 군데에 타일을 채움
	tile_num += 1
	if isComplete(row, col, size):
		showerRoom[row + size - 1][col + size - 1] = tile_num
	if isComplete(row + size, col, size):
		showerRoom[row + size][col + size - 1] = tile_num
	if isComplete(row, col + size, size):
		showerRoom[row + size - 1][col + size] = tile_num
	if isComplete(row + size, col + size, size):
		showerRoom[row + size][col + size] = tile_num
	# 이제 재귀
	tile(row, col, size)
	tile(row + size, col, size)
	tile(row, col + size, size)
	tile(row + size, col + size, size)

# input
k = 2 ** int(input())
drain = tuple(map(int, input().split()))
# process
'''
L-트로미노 문제.
정사각형을 4등분해서 네 개의 사분면으로 만든다.
네 개의 사분면 중 완전한(:= 배수구가 없거나 타일이 하나도 채워지지 않은) 사분면 세 개가
서로 맞닿는 부분을 ㄴ자 타일로 덮어서 세 사분면도 완전하지 않게 만든다.
이후 각각 재귀.
'''
showerRoom = [[0 for _ in range(k)] for _ in range(k)]
showerRoom[k - drain[1]][drain[0] - 1] = -1
tile_num = 0
tile(0, 0, k)
# output
for line in showerRoom:
	print(*line)