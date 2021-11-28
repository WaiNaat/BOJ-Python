### 시간 초과 ###

import sys
input = sys.stdin.readline

'''
슬라이딩 윈도우 알고리즘 사용
'''
def slidingWindow(w, k):
	short = 10001
	long = 0
	wLen = len(w)
	for i in range(k, wLen):
		# 창문 초기화
		left = 0
		right = i-1
		start = ord(w[left]) - 97
		end = ord(w[right]) - 97
		chCnt = {i:0 for i in range(0, 26)}
		for j in range(left, right+1):
			chCnt[ord(w[j]) - 97] += 1

		while 1:
			# 시작문자=끝문자 이고 그게 k개 들어 있을 때
			if start == end and chCnt[start] == k:
				long = i
				if i < short: short = i
			# 창문 이동
			left += 1
			right += 1
			if right >= wLen: break
			chCnt[start] -= 1
			start = ord(w[left]) - 97
			end = ord(w[right]) - 97
			chCnt[end] += 1
	return (short, long)

# input
T = int(input())
for _ in range(T):
	W = list(input().rstrip())
	K = int(input())
# process
	sol1, sol2 = slidingWindow(W, K)
# output
	print(sol1, sol2) if sol1 != 10001 and sol2 != 0 else print(-1)