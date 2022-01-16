import sys
input = sys.stdin.readline
# input
row, col = map(int, input().split())
puzzle = [input().rstrip() for _ in range(row)]

# process
'''
가로줄 보면서 확인, 세로줄 보면서 확인.
단어는 알파벳 두 개 이상이어야 함.
'''
# padding 추가
for i in range(row): puzzle[i] += '#'
row += 1
col += 1
puzzle.append("".join(['#' for _ in range(col)]))

sol = "zzzzzzzzzzzzzzzzzzzzz" # 21개
word = []
# 가로줄
for r in range(row):
	for c in range(col):
		cur = puzzle[r][c]
		if cur == '#':
			if len(word) >= 2:
				word = "".join(word)
				if word < sol: sol = word
			word = []
		else:
			word.append(cur)
# 세로줄
for c in range(col):
	for r in range(row):
		cur = puzzle[r][c]
		if cur == '#':
			if len(word) >= 2:
				word = "".join(word)
				if word < sol: sol = word
			word = []
		else:
			word.append(cur)

# output
print(sol)