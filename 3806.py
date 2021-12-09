### 틀렸습니다 ###

import sys
input = sys.stdin.readline

# INPUT
T = int(input())
for k in range(1, T+1):
	S = list(input().rstrip())
	T = list(input().rstrip())
# PROCESS
	'''
	1. s0t1 과 s1t0 은 서로 교환
	2. s0t1 을 s1t1 로 변환
	3. s?t1 과 s1t0 을 서로 교환
	4. ?들을 알맞게 변형
	'''
	sLen = len(S)
	s0t1 = 0
	s1t0 = 0
	s_t0 = 0
	s_t1 = 0
	for i in range(sLen):
		s, t = S[i], T[i]
		if   s == '0' and t == '1': s0t1 += 1
		elif s == '1' and t == '0': s1t0 += 1
		elif s == '?' and t == '0': s_t0 += 1
		elif s == '?' and t == '1': s_t1 += 1
	
	cnt = 0
	
	exchange = min(s0t1, s1t0)
	cnt += exchange
	s0t1 -= exchange
	s1t0 -= exchange

	cnt += s0t1
	s0t1 = 0

	exchange = min(s_t1, s1t0)
	s_t1 -= exchange
	s1t0 -= exchange
	s_t0 += exchange

	cnt += s_t0 + s_t1
# OUTPUT
	if s0t1 == 0 and s1t0 == 0:
		print("case %d: %d" % (k, cnt))
	else:
		print("case %d: -1" % k)