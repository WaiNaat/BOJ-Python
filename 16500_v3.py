import sys
input = sys.stdin.readline

# input
S = input().rstrip()
N = int(input())
A = [input().rstrip() for _ in range(N)]

# process
'''동적 계획법
OPT(i) := S[i:] 를 A의 단어들로 만들 수 있으면 True

OPT(i)=False일 때
	A의 어떤 단어 word에 대해
	S[i : i + len(word)] = word이고 OPT(i+len(word)) = True면 OPT(i)도 True
'''
opt = [False for _ in range(len(S))]
for i in range(len(S)-1, -1, -1):
	if opt[i] is True: continue
	for word in A:
		wLen = len(word)
		if S[i:] == word or \
			(i+wLen < len(S) and S[i : i+wLen] == word and opt[i+wLen] is True):
			opt[i] = True
			break

# output
print(1) if opt[0] else print(0)