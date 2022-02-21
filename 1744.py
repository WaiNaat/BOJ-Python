import sys
input = sys.stdin.readline

# input
n = int(input())
num_positive = []
num_negative = []
for _ in range(n):
	val = int(input())
	if val > 0: num_positive.append(val)
	else: num_negative.append(val)

# process
'''
양수는 큰 거 두개씩 묶는다.
양수가 아닌 수는 작은거 두개씩 묶는다.
양수와 양수가 아닌 수는 절대 같이 묶지 않는다.
양수에서 묶는 수 둘 중 하나가 1일 경우 묶지 않는다.
'''
sol = 0

# 양수
num_positive.sort()
while len(num_positive) > 1:
	val1 = num_positive.pop()
	val2 = num_positive.pop()
	if val1 == 1 or val2 == 1:
		sol += val1 + val2
	else:
		sol += val1 * val2
sol += sum(num_positive)

# 양수가 아닌 수
num_negative.sort(reverse = True)
while len(num_negative) > 1:
	sol += num_negative.pop() * num_negative.pop()
sol += sum(num_negative)

# output
print(sol)