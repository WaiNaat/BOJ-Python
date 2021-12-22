import sys
input = sys.stdin.readline
# functions
'''
digitSquere() := 자리수의 제곱의 합을 return
'''
def digitSquare(val:int):
	val = map(int, tuple(str(val)))
	ret = 0
	for i in val:
		ret += i ** 2
	return ret

# input
x, y = map(int, input().split())
# process
'''
max(A)=max(B)=999,999,999
digitSquare(999,999,999)=729 이므로 숫자가 크게 줄어들어
어떤 사이클을 금방 얻을 수 있음 >> 완전탐색 사용 가능?

xSeq := x부터 시작하는 수열.
ySeq := y부터 시작하는 수열.
found[i]=(xIdx, yIdx) := xSeq[xIdx]=ySeq[yIdx] 라는 뜻.
'''
while x != 0:
	xSeq = [x]
	ySeq = [y]
	# x의 수열 계산.
	while True:
		val = digitSquare(xSeq[-1])
		if val in xSeq: break
		xSeq.append(val)
	# y의 수열을 계산하면서 xSeq랑 겹치는 부분이 있는지도 계산.
	sol = 0
	while True:
		val = ySeq[-1]
		for i in range(len(xSeq)):
			if xSeq[i] == val:
				# 겹치는 게 있으면 수열의 길이의 합의 최솟값을 업데이트.
				length = i + 1 + len(ySeq)
				if sol == 0: sol = length
				elif sol > length: sol = length
		val = digitSquare(val)
		if val in ySeq: break
		ySeq.append(val)
	
# output & input
	print(x, y, sol)
	x, y = map(int, input().split())