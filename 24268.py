### 시간 초과 ###

from collections import Counter
# input
n, d = map(int, input().split())
# process
'''
d진법 계산기 필요.
숫자의 등장 횟수를 세는 데는 큰 시간이 필요하지 않음.
완전탐색으로 N 초과의 수를 하나씩 찾아보면 됨.
만약 숫자의 자리수가 d를 넘어가면 '모두 정확히 한 번'등장 불가.

val := n을 d진법으로 변환한 수. d^x의 자리는 val[x]로 찾을 수 있음.
'''
# n을 d진법으로 변환.
tmp = n
# d진법으로 몇 자리 수인지 계산
i = 0
while d ** i <= tmp: i += 1
val = [0 for _ in range(i)]
# 각 자리수 계산
while tmp > 0:
	i -= 1
	num = 0
	digit = d ** i
	while num * digit <= tmp: num += 1
	num -= 1
	val[i] = num
	tmp -= num * digit

found = None
while True:
	# val에 1을 더함.
	add_1 = True
	i = 0
	while add_1:
		val[i] += 1
		if val[i] == d:
			val[i] = 0
			i += 1
			if i == len(val): val.append(0)
		else:
			add_1 = False

	# '정확히 한 번' 조건에 부합하는지 확인
	if len(val) > d:
		found = False
		break
	else:
		found = True
		num_cnt = Counter(val)
		for i in range(d):
			if num_cnt[i] != 1:
				found = False
				break
		if found: break

# val을 10진법으로 다시 변환
sol = -1
if found:
	sol = 0
	for i in range(len(val)):
		sol += val[i] * (d ** i)

# output
print(sol)