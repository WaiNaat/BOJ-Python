### 시간 초과 ###

'''
일단 백트래킹으로 구현
S에 들어있는 A와 B의 개수, T에 들어있는 A와 B의 개수를 비교
>> 두 연산이 각각 몇번 쓰여야 하는지 알 수 있음
'''
import sys
input = sys.stdin.readline

# function
def solve(oper_A, oper_B):
	# base case
	if oper_A + oper_B == 0:
		if S == T:
			return 1
		else:
			return 0

	# recursive step
	if oper_A > 0:
		S.append('A')
		if solve(oper_A - 1, oper_B) == 1:
			return 1
		S.pop()
	if oper_B > 0:
		S.append('B')
		S.reverse()
		if solve(oper_A, oper_B - 1) == 1:
			return 1
		S.reverse()
		S.pop()
	return 0

# input
S = list(input().rstrip())
T = list(input().rstrip())

# process
# 각 연산이 몇번 사용되는지 계산
oper_A = 0
oper_B = 0

for c in S:
	if c == 'A': oper_A -= 1
	else: oper_B -= 1
for c in T:
	if c == 'A': oper_A += 1
	else: oper_B += 1
print(oper_A, oper_B)
sol = solve(oper_A, oper_B) if oper_A >= 0 and oper_B >= 0 else 0

# output
print(sol)