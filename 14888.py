### 시간 초과 ###

from itertools import permutations
# functions
div = lambda a, b: -(-a//b) if a<0 else a//b

# input
N = int(input())
A = tuple(map(int, input().split()))
operators = tuple(map(int, input().split()))
# process
'''
max(N)=11이므로 10개의 연산자를 배치하는 순서는 10!개
	따라서 완전탐색 알고리즘 사용 가능.

10! =360만, 각 iter당 elt oper 20개? 좀 많긴 하네
'''
operators = ['+'] * operators[0] + \
			['-'] * operators[1] + \
			['*'] * operators[2] + \
			['/'] * operators[3]

result_max = -1000000001
result_min = 1000000001
for operList in permutations(operators):
	operand = A[0]
	for i in range(N - 1):
		oper = operList[i]
		if oper == '+':
			operand += A[i + 1]
		elif oper == '-':
			operand -= A[i + 1]
		elif oper == '*':
			operand *= A[i + 1]
		else: # '/'
			operand = div(operand, A[i + 1])
	result_max = max(operand, result_max)
	result_min = min(operand, result_min)
# output
print(result_max)
print(result_min)