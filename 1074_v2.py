import sys
sys.setrecursionlimit(10 ** 6)
# function
def zSearch(row, col, size):
	'''
	row, col 위치부터 size*size크기의 배열을 본다.
	찾고자 하는 r, c값이 몇 사분면인지 판단한다.
	그러면 그 r, c값 앞에 적어도 몇 개의 숫자가 더 있는지 알 수 있다.
	해당 사분면으로 재귀해서 반복한다.
	'''
	global cnt, r, c
	# base case
	if size == 1:
		cnt += 1
		return
	# recursive step
	size //= 2
	# r, c가 좌상단 사분면에 위치
	if row <= r < row + size and col <= c < col + size:
		return zSearch(row, col, size)
	# r, c가 우상단 사분면에 위치
	elif row <= r < row + size and col + size <= c < col + 2 * size:
		cnt += size * size
		return zSearch(row, col + size, size)
	# r, c가 좌하단 사분면에 위치
	elif row + size <= r < row + size * 2 and col <= c < col + size:
		cnt += 2 * size * size
		return zSearch(row + size, col, size)
	# r, c가 우하단 사분면에 위치
	else:
		cnt += 3 * size * size
		return zSearch(row + size, col + size, size)

# input
n, r, c = map(int, input().split())
# process
cnt = -1
zSearch(0, 0, pow(2, n))
# output
print(cnt)