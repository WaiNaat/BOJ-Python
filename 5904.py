import sys
sys.setrecursionlimit(10 ** 6)
# function
def moo(k, n, start, mooLen):
	'''
	start := 여기부터 mooLen 길이의 S(k)를 살펴본다.
	midLen := m 하나와 o가 k+2개인 수열의 길이
	partitionLen := S(k-1)의 길이
	'''
	# base case
	if k == 0:
		if n == start: return 'm'
		else: return 'o'
	# recursive step
	midLen = k + 3
	partitionLen = (mooLen - midLen) // 2
	
	if start + partitionLen == n:
		return 'm'
	elif start + partitionLen < n < start + partitionLen + midLen:
		return 'o'
	elif n < start + partitionLen:
		return moo(k - 1, n, start, partitionLen)
	else:
		return moo(k - 1, n, start + partitionLen + midLen, partitionLen)

# input
n = int(input())
# process & output
'''
moo 수열을 생성 방식에 따라 3등분해서
n이 그 3등분 조각 중 어디에 있는지 찾는다.
만약 가운데에 있으면 m 또는 o가 바로 나옴.
아니면 S(k-1)로 재귀하면 됨.

k는 어떻게 찾지?
moo 수열의 길이?
3 > 10 > 25 > 56
  7    15   31
2^3-1  2^4-1  2^5-1
2^31 = 2,147,483,648이므로
n <= len(S(k))인 k는 금방 찾음.
'''
# k 구하기
i = 2
k = -1
mooLen = 0
while mooLen <= n:
	mooLen += pow(2, i) - 1
	k += 1
	i += 1
# moo 수열은 0번 idx부터 시작한다고 가정
print(moo(k, n - 1, 0, mooLen))