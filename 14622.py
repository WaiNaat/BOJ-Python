import sys
input = sys.stdin.readline
import heapq as hq
# function
def isPrime(value):
	'''
	value가 소수인지 판별하는 함수.
	'''
	if value == 0 or value == 1: return False
	for i in range(2, value):
		if i * i > value: break
		if value % i == 0: return False
	return True

# input
dw_said = []
gs_said = []
said_primes = set()
dw_score = gs_score = 0

n = int(input())
for _ in range(n):
	dw, gs = map(int, input().split())
# process
	'''
	한 사람당 최대 힙 1개: 말한 소수를 크기별로 정렬할 필요
	집합: 두 사람이 말한 소수를 저장할 필요
	'''
	# 대웅씨 차례
	# 3.
	if dw in said_primes:
		dw_score -= 1000
	# 2.
	elif not isPrime(dw):
		if len(gs_said) < 3: gs_score += 1000
		else:
			tmp1 = hq.heappop(gs_said)
			tmp2 = hq.heappop(gs_said)
			gs_score -= gs_said[0]
			hq.heappush(gs_said, tmp1)
			hq.heappush(gs_said, tmp2)
	else:
		hq.heappush(dw_said, -dw)
		said_primes.add(dw)

	# 규성씨 차례
	# 3.
	if gs in said_primes:
		gs_score -= 1000
	# 2.
	elif not isPrime(gs):
		if len(dw_said) < 3: dw_score += 1000
		else:
			tmp1 = hq.heappop(dw_said)
			tmp2 = hq.heappop(dw_said)
			dw_score -= dw_said[0]
			hq.heappush(dw_said, tmp1)
			hq.heappush(dw_said, tmp2)
	else:
		hq.heappush(gs_said, -gs)
		said_primes.add(gs)
# output
if dw_score > gs_score: print("소수의 신 갓대웅")
elif dw_score == gs_score: print("우열을 가릴 수 없음")
else: print("소수 마스터 갓규성")