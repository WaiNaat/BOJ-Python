### 시간 초과 ###
'''
하나씩 방문하면 안 되고
4분할 중에 어느 위치인지를 찾아서 들어가야 하나?
'''

import sys
sys.setrecursionlimit(10 ** 6)
# function
def zSearch(row, col, size):
	'''
	row, col 위치부터 size*size크기의 배열을
	주어진 순서대로 방문.
	만약 찾고자 하는 위치를 찾았으면 True 반환.
	'''
	global cnt
	# base case
	if size == 1:
		cnt += 1
		return True if row == r and col == c else False
	# recursive step
	size //= 2
	found = zSearch(row, col, size)
	if not found: found = zSearch(row, col + size, size)
	if not found: found = zSearch(row + size, col, size)
	if not found: found = zSearch(row + size, col + size, size)
	return found

# input
n, r, c = map(int, input().split())
# process
cnt = -1
zSearch(0, 0, pow(2, n))
# output
print(cnt)