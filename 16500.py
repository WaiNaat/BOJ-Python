### 시간 초과 ###

import sys
input = sys.stdin.readline
from collections import deque

# input
S = input().rstrip()
N = int(input())
A = [input().rstrip() for _ in range(N)]

# process
'''
큐를 사용
pop: A안의 모든 단어들에 대해 pop된 문자열의 첫 부분이
	그 단어인지 확인. 만약 맞으면 그 부분을 제외한 나머지를 push
	
	만약 pop된 단어가 빈 문자열이면 S를 만들었단 뜻이니 성공
	큐가 완전히 비어버렸으면 실패
'''
q = deque([S])
isSuccess = 0
while q:
	candidate = q.popleft()
	candiLen = len(candidate)

	if candiLen == 0:
		isSuccess = 1
		break

	for word in A:
		wordLen = len(word)
		if wordLen > candiLen:
			continue
		if word == candidate[:wordLen]:
			q.append(candidate[wordLen:])

# output
print(isSuccess)