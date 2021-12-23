### 시간 초과 ###

# input
X = int(input())
word = list(input())
# process
'''
무식하게 원래 단어를 복원함.
flag := True면 변화 이전에 앞 부분 절반이었고 False면 뒷 부분 절반 소속이었음
cnt := 이 글자가 앞에서부터 몇 번째 단어였는지 세는 변수
'''
wLen = len(word)
half = wLen // 2
for _ in range(X):
	word2 = [0 for _ in range(wLen)]
	flag = True
	cnt = 0
	for ch in word:
		if flag:
			word2[cnt] = ch
		else:
			word2[wLen - 1 - cnt] = ch
			cnt += 1
		flag = not flag
	word = word2
# output
print(''.join(word))