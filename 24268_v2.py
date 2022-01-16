### 틀렸습니다 ###

from collections import Counter
# input
n, d = map(int, input().split())
# process
'''
n을 d진법으로 바꾼다.
문제의 조건에 맞추려면 무조건 d진법의 d자리 수여야 함.
>> 시작점을 n 또는 d진법 d자리 수 중 가장 작은 녀석 둘 중 큰 친구로.

val := n을 d진법으로 변환한 수. d^x의 자리는 val[x]로 찾을 수 있음.
'''
found = False
outOfRange = False
# n을 d진법으로 변환.
tmp = n
# d진법으로 몇 자리 수인지 계산
i = 0
while d ** i <= tmp: i += 1
val = [0 for _ in range(d)]
if i == d:
	# 각 자리수 계산
	while tmp > 0:
		i -= 1
		num = 0
		digit = d ** i
		while num * digit <= tmp: num += 1
		num -= 1
		val[i] = num
		tmp -= num * digit
elif i < d:
	val[d - 1] = 1
else: 
	outOfRange = True

while not found and not outOfRange:
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
		outOfRange = True
	else:
		found = True
		num_cnt = Counter(val)
		for i in range(d):
			if num_cnt[i] != 1:
				found = False
				break

print(val)

# val을 10진법으로 다시 변환
sol = -1
if found:
	sol = 0
	for i in range(len(val)):
		sol += val[i] * (d ** i)

# output
print(sol)