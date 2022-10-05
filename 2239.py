### python3 시간초과, pypy 통과 ###

'''
백트래킹
빈칸이 없을 경우가 base case

처음에 빈칸이 어디있는지 센 후에
빈칸을 앞에서부터 채운다는 느낌으로
'''
import sys
input = sys.stdin.readline

# function
def fill_sudoku(idx):
	# base case
	if idx >= len(empty):
		return True

	# recursive step
	r, c = empty[idx]
	candidates = find_possible_numbers(r, c)
	for candidate in candidates:
		board[r][c] = candidate
		if fill_sudoku(idx + 1):
			return True
		board[r][c] = 0
	return False

def find_possible_numbers(r, c):
	candidates = set(i for i in range(1, 10))
	
	for c2 in range(9):
		if board[r][c2] in candidates:
			candidates.remove(board[r][c2])
	
	for r2 in range(9):
		if board[r2][c] in candidates:
			candidates.remove(board[r2][c])
		
	base_r = int(r / 3)
	base_c = int(c / 3)
	for r2 in range(base_r * 3, base_r * 3 + 3):
		for c2 in range(base_c * 3, base_c * 3 + 3):
			if board[r2][c2] in candidates:
				candidates.remove(board[r2][c2])

	return candidates

# input
board = [list(map(int, list(input().rstrip()))) for _ in range(9)]

# process
empty = []
for r in range(9):
	for c in range(9):
		if board[r][c] == 0:
			empty.append((r, c))

fill_sudoku(0)

# output
sol = []
for line in board:
	sol.append(''.join(map(str, line)))
print('\n'.join(sol))