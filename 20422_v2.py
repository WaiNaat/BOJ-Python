# input
S = list(input())
# process
'''
1.
대칭이 없는 대문자/소문자를 동일한 소문자/대문자로 바꿨을 때 대칭이 생기면 바꿔줌.
	대상: (B, D, L, N, P, Q, R, a, e, h, s, t, y, z)
대칭이 있다고 해도 'oO'로 만드는 퀼린드롬 닉은 가장 짧은 'oo'여야 함.
	>> 대소문자가 모두 대칭이 있으면 소문자로 통일함.
	대상: (I, M, O, U, V, W, X)

2.
S의 거울상 mirror를 만듦 (만들 수 없으면 퀼린드롬 X)

3.
S와 S_mirror를 이어서 새로운 닉네임을 만드는데
	이 때 겹치는 부분이 있으면 겹치도록 이어줌.

change[ch] := ch의 대칭 문자.
change_upper := 이 안의 것들은 소문자로 바꾸면 대칭이 있음.
change_upper := 이 안의 것들은 대문자로 바꾸면 대칭이 있음.
isQuilin := True면 퀼린드롬이 있음.
overlapIdx := mirror[ :overlapIdx]만큼은 S의 뒷부분과 겹침.
'''
# 대칭표 만들기
original	= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
change 		= "A---3--HI---M-O---2TUVWXY5-d-b----i--lmnoqp7--uvwx--01SE-Z-r8-"
change = {original[i]:change[i] for i in range(len(original))}

change_upper = "BDLNRPQRIMOUVWX"
change_lower = "aehstyz"

sLen = len(S)
mirror = ['-' for _ in range(sLen)]
isQuilin = True
for i in range(sLen):
	# 1.
	if S[i] in change_upper: S[i] = S[i].lower()
	elif S[i] in change_lower: S[i] = S[i].upper()
	# 2.
	if change[S[i]] == '-':
		isQuilin = False
		break
	mirror[-1-i] = change[S[i]]

# 3.
if isQuilin:
	S = "".join(S)
	mirror = "".join(mirror)
	overlapIdx = 0
	for i in range(sLen):
		if S[i:] == mirror[:sLen-i]:
			overlapIdx = sLen-i
			break
	S += mirror[overlapIdx:]

# output
print(S) if isQuilin else print(-1)