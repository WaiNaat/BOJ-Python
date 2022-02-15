from math import log2, ceil
import sys
sys.setrecursionlimit(10 ** 6)
# function
def thueMorse(k, reverse = False):
	'''
	투에모스 문자열을 반으로 갈라서 k가 왼쪽인지 오른쪽인지 찾는다.
	왼쪽에서 a번째면 왼쪽으로 재귀
	오른쪽에서 a번째면 왼쪽 a번째 값이라 치고 그 반대를 출력
	'''
	# base case
	if k == 1:
		return 1 if reverse else 0
	elif k == 2:
		return 0 if reverse else 1
	# recursive step
	n = ceil(log2(k)) - 1
	if k <= 2 ** n:
		return thueMorse(k, reverse)
	else:
		return thueMorse(k - 2 ** n, not reverse)

# input
k = int(input())
# process & output
print(thueMorse(k))