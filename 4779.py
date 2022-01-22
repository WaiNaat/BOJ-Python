import sys
input = sys.stdin.readline
# function
def cantor(start, size):
	'''
	base case: size가 1이면 끝
	recursive step:
		size를 3등분해서 중앙을 공백으로 바꾸고 재귀
	'''
	if size == 1: return

	size //= 3
	for i in range(start + size, start + size * 2):
		line[i] = ' '
	cantor(start, size)
	cantor(start + 2 * size, size)

# input
n = input()
while n != '':
	n = int(n)
# process
	line = ['-' for _ in range(pow(3, n))]
	cantor(0, pow(3, n))
# output
	print("".join(line))
	n = input()