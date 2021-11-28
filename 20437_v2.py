import sys
input = sys.stdin.readline

# input
T = int(input())
for _ in range(T):
	W = list(input().rstrip())
	K = int(input())
# process
	short = 10001
	long = 0

	# 각 알파벳이 등장한 위치를 알파벳별로 저장
	alphabets = [[] for _ in range(26)]
	for i in range(len(W)):
		alphabets[ord(W[i]) - 97].append(i)

	# K 이상 등장한 알파벳들에 대해 가능한 연속 문자열 길이 계산(슬라이딩 윈도우)
	for alphabet in alphabets:
		aLen = len(alphabet)
		if aLen < K: continue

		left = 0
		right = K - 1
		while 1:
			# 연속 문자열 길이 계산
			length = alphabet[right] - alphabet[left] + 1
			if long < length: long = length
			if length < short: short = length
			# 창문 이동
			left += 1
			right += 1
			if right >= aLen: break
# output
	print(short, long) if short != 10001 and long != 0 else print(-1)