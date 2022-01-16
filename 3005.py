import sys
input = sys.stdin.readline
# input
row, col = map(int, input().split())
puzzle = [input().rstrip() for _ in range(row)]
# process
'''
가로로 모든 줄 확인, 세로로 모든 줄 확인.
그 후 단어를 정렬하면 됨.
단어를 볼 때 #이 나오면 단어의 끝과 시작이고
단어는 최소 두 글자라는 것을 확인하기.
'''
words = []
sharp = False
aux = []
# 가로
for r in range(row):
	for c in range(col):
		cur = puzzle[r][c]
		if cur == '#':
			if len(aux) >= 2:
				words.append("".join(aux))
			aux = []
		else:
			aux.append(cur)
	if len(aux) >= 2:
		words.append("".join(aux))
	aux = []
# 세로
for c in range(col):
	for r in range(row):
		cur = puzzle[r][c]
		if cur == '#':	
			if len(aux) >= 2:
				words.append("".join(aux))
			aux = []
		else:
			aux.append(cur)
	if len(aux) >= 2:
		words.append("".join(aux))
	aux = []
# output
words.sort()
print(words[0])