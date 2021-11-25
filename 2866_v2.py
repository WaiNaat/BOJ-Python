import sys
input = sys.stdin.readline

# function
'''
isEqualCol()
	input : 시작 행과 끝 행
	output : 열을 읽었을 때 문자열이 중복되면 True, 아니면 False
'''
def isEqualCol(start, end):
	strings = set([])
	for col in range(c):
		s = ''.join([words[row][col] for row in range(start, end)])
		if s in strings: 
			return True
		strings.add(s)
	return False
'''
equalCol()
	input : 탐색 시작 행과 끝 행, 전체 표의 끝 행
	output : 이분 탐색 사용, 열을 읽었을 때 문자열이 중복되지 않는 열 중 가장 큰 값
'''
def equalCol(left, right, end):
	# 만약 right가 0 이하가 되면 모든 경우에 대해 문자열이 중복이란 뜻
	if right <= 0: return 0

	mid = int((left + right) / 2)
	me = isEqualCol(mid, end)
	next = isEqualCol(mid + 1, end)
	# 나부터 열을 본 게 중복이면 답은 일단 나보다 위쪽의 행에 있음
	if me: return equalCol(left, mid - 1, end)
	# 나와 내 다음 둘 다 중복되는 게 없으면 답은 일단 나보다 아래쪽 행에 있음
	elif not me and not next: return equalCol(mid + 1, right, end)
	# 둘 다 아니면 내가 답
	else: return mid


# input
r, c = map(int, input().split())
words = [list(input().rstrip()) for _ in range(r)]
# process & output
print(equalCol(1, r, r))