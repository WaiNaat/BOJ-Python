'''
어느 하나의 연산자를 기준으로 수식을 왼쪽과 오른쪽을 나눌 수 있음
왼쪽의 최댓값/최솟값과 오른쪽의 최댓값/최솟값을 조합해서 수식의 최솟값/최댓값을 찾을 수 있음

opt({MIN|MAX}, i, j) := i번 숫자부터 j번 숫자까지 계산했을 때 최댓값/최솟값
operator(k, val1, val2) := k번째 연산자로 val1과 val2를 계산

opt(MIN, i, j) = 
	operator(k, opt(MIN, i, k), opt(MIN, k+1, j) )
	operator(k, opt(MIN, i, k), opt(MAX, k+1, j) )
	operator(k, opt(MAX, i, k), opt(MIN, k+1, j) )
	operator(k, opt(MAX, i, k), opt(MAX, k+1, j) )
	단, k는 i <= k < j 인 정수
	이 값들 중 최솟값.

계산 순서
식 길이가 짧은 순서대로
'''
import sys
input = sys.stdin.readline

# functions
def calc(operator, val1, val2):
	if operator == '+':
		return val1 + val2
	elif operator == '-':
		return val1 - val2
	else:
		return val1 * val2

# input
N = int(input())
equation = input().strip()

# process
# 연산자와 피연산자 분리
operator = []
operand = []
for i in range(N):
	if i % 2 == 0:
		operand.append(int(equation[i]))
	else:
		operator.append(equation[i])

# opt 배열 만들고 초기화
opt_max = [[-2147483647 for _ in range(len(operand))] for _ in range(len(operand))]
opt_min = [[2147483647 for _ in range(len(operand))] for _ in range(len(operand))]

# 계산
for i in range(len(operand)):
	opt_max[i][i] = operand[i]
	opt_min[i][i] = operand[i]
	
for length in range(1, len(operand)):

	for left in range(len(operand)):
		right = left + length

		if right >= len(operand):
			break

		for mid in range(left, right):
			
			values = [
				calc(operator[mid], opt_max[left][mid], opt_max[mid + 1][right]),
				calc(operator[mid], opt_min[left][mid], opt_max[mid + 1][right]),
				calc(operator[mid], opt_max[left][mid], opt_min[mid + 1][right]),
				calc(operator[mid], opt_min[left][mid], opt_min[mid + 1][right])
			]

			opt_max[left][right] = max(opt_max[left][right], max(values))
			opt_min[left][right] = min(opt_min[left][right], min(values))

# output
print(opt_max[0][len(operand) - 1])