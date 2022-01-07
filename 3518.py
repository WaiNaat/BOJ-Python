import sys
input = sys.stdin.readline

# input
doc = []
lineNum = 0
maxWord = 0
line = input()
while line != "":
	line = line.split()
	doc.append(line)
	maxWord = max(len(line), maxWord)
	lineNum += 1
	line = input()

# process
for i in range(maxWord-1):
	maxLen = 0
	for j in range(lineNum):
		if len(doc[j]) < i+1: continue # 각 line의 i번째 단어에 대해서 계산하는 건데 i번째 단어가 없는 line의 경우 패스
		maxLen = max(len(doc[j][i]), maxLen)

	for j in range(lineNum):
		if len(doc[j]) <= i+1: continue # 각 line의 마지막 단어에는 띄어쓰기 필요 없음
		diff = maxLen - len(doc[j][i])
		doc[j][i] += " " * diff

# output
for line in doc:
	sys.stdout.write(' '.join(line))
	sys.stdout.write('\n')