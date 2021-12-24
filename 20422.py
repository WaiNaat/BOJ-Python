### 틀렸습니다 ###

from collections import deque
# functions
'''
문자열 S + tail 이 퀼린드롬인지 판별.
'''
def isQilin():
	s = "".join(["".join(S), "".join(tail)])
	for i in range(len(s) // 2 + 1):
		if change[s[i]] != s[-1-i] and s[-1-i] != '-':
			return False
	return True

# input
S = list(input())
# process
'''
1.
대칭이 없는 대문자/소문자를 동일한 소문자/대문자로 바꿨을 때 대칭이 생기면 일단 바꿔줌.
대상: (B, D, L, N, P, Q, R, a, e, h, s, t, y, z)

2.
새로운 닉네임은 S + tail로 구성됨
문자열 tail은 S+tail이 퀼린드롬이 되기 위해 추가해야 하는 글자들임.
i in range(len(S)) 에 대해
	S + tail 이 퀼린드롬이 아니면
	S[i]의 대칭을 tail의 앞부분에 추가
'''
# 1.
change_upper = "BDLNRPQR"
change_lower = "aehstyz"
for i in range(len(S)):
	if S[i] in change_upper: S[i] = S[i].lower()
	elif S[i] in change_lower: S[i] = S[i].upper()
# 거울대칭표 만들기
original 	= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
change 		= "A---3--HI---M-O---2TUVWXY5-d-b----i--lmnoqp7--uvwx--01SE-Z-r8-"
change = {original[i]:change[i] for i in range(len(original))}
# 2.
sLen = len(S)
tail = deque([])
for i in range(sLen):
	found = isQilin()
	if found or change[S[i]] == '-': break
	tail.appendleft(change[S[i]])
found = isQilin()
# output
print("".join(["".join(S), "".join(tail)])) if found else print(-1)