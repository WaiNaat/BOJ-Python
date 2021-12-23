# input
X = int(input())
word = input()
# process
'''
설마 단어가 돌고 도나? 예제는 일단 그럼
acefdb, aedbfc, adfcbe, afbecd, abcdef, / acefdb, ...
'''
seq = [word]
wLen = len(word)
half = wLen // 2
cycle = False
for _ in range(X):
	# 눈을 깜빡이기 한 단계 전으로 되돌린다.
	word2 = [0 for _ in range(wLen)]
	flag = True
	cnt = 0
	for ch in seq[-1]:
		if flag:
			word2[cnt] = ch
		else:
			word2[wLen - 1 - cnt] = ch
			cnt += 1
		flag = not flag
	word2 = "".join(word2)
	# 사이클이 완성되었는지 확인
	if word2 in seq:
		cycle = True
	else:
		seq.append(word2)
	if cycle: break
# output
print(seq[X % len(seq)]) if cycle else print(seq[-1])