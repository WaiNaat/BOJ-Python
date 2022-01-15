import sys
input = sys.stdin.readline
from collections import deque
# input & process
'''
모양수열을 일종의 '회전하는 큐'로 생각해서
회전해서 같은 숫자 배열을 가지는 모양수열은 전부 같은 모양이다.
>> 모양수열의 길이가 최대 50이므로
최대 50개의 같은 모양들을 집합에 저장해서 판단 가능.

이동방향이 표본 모양수열과 완전히 반대여도 같은 다각형.
'''
n = int(input())
sample = deque(input().split())
# 역방향
sample_reverse = deque()
for dir in sample:
	if dir == '1': sample_reverse.appendleft('3')
	elif dir == '2': sample_reverse.appendleft('4')
	elif dir == '3': sample_reverse.appendleft('1')
	elif dir == '4': sample_reverse.appendleft('2')

# 같은 모양들 모음
polygon = set()
polygon.add("".join(sample))
polygon.add("".join(sample_reverse))
for _ in range(n):
	sample.append(sample.popleft())
	sample_reverse.append(sample_reverse.popleft())
	polygon.add("".join(sample))
	polygon.add("".join(sample_reverse))

# 입력값들에 대해 검사
sol = []
seq_num = int(input())
for _ in range(seq_num):
	seq = input().split()
	if "".join(seq) in polygon:
		sol.append(seq)

# output
print(len(sol))
for seq in sol: print(*seq)