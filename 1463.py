# input
n = int(input())
# process
'''
숫자 n에 대한 최소 연산 횟수를 opt(n)이라 하면
opt(n) = 
	opt(n-1) + 1 (n이 홀수 또는 3으로 나눈 나머지가 1)
	opt(n-2) + 2 (n을 3으로 나눈 나머지가 2)
	opt(n/2) (n이 짝수)
	opt(n/3) (n이 3의 배수)
	이 네 가지 경우 중 가장 작은 값.
'''
opt = [0 for _ in range(max(4, n + 1))]
opt[1] = 0
opt[2] = 1
opt[3] = 1

for i in range(4, n + 1):
	values = []
	if i % 2 == 1 or i % 3 == 1:
		values.append(opt[i - 1] + 1)
	if i % 3 == 2:
		values.append(opt[i - 2] + 2)
	if i % 2 == 0:
		values.append(opt[i // 2] + 1)
	if i % 3 == 0:
		values.append(opt[i // 3] + 1)
	opt[i] = min(values)
# output
print(opt[n])