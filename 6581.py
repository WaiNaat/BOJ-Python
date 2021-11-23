import sys
input = sys.stdin.readlines
print = sys.stdout.write

# init
document = ''.join(input()).split()
colCnt = 0
hr = ''.join(['-' for _ in  range(80)])

# process
for word in document:
	# 태그 처리
	if word == "<br>":
		print("\n")
		colCnt = 0
	elif word == "<hr>":
		print("\n%s\n" % hr) if colCnt != 0 else print("%s\n" % hr)
		colCnt = 0
	# 단어 처리
	else:
		# 공백 필요 여부 판단
		needSpace = False
		if colCnt != 0:
			colCnt += 1
			needSpace = True
		colCnt += len(word)
		# 줄바꿈 판단
		if colCnt > 80:
			print("\n%s" % word)
			colCnt = len(word)
		# 공백 및 단어 출력
		else:
			if needSpace: 
				print(' ')
			print(word)
print('\n')