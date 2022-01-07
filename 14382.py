import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
	N = int(input())

	if N == 0:
		print("Case #%d: INSOMNIA" % (i+1))
		continue

	num = set([1,2,3,4,5,6,7,7,8,9,0])
	aN = 0
	while len(num) > 0:
		aN = int(aN) + N
		aN = str(aN)
		for j in range(len(aN)):
			if int(aN[j]) in num: num.remove(int(aN[j]))
			
	print("Case #%d: %s" % (i+1, aN))