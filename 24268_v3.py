from itertools import permutations
# input
n, d = map(int, input().split())
# process
'''
n을 d진법으로 바꾼다.
문제의 조건에 맞추려면 무조건 d진법의 d자리 수여야 함.

val := n을 d진법으로 변환한 수. d^x의 자리는 val[x]로 찾을 수 있음.

조건을 만족하는 d진법 d자리 수 >> 순열로 구함.
'''
# n이 d진법으로 몇 자리 수인지 계산
i = 0
while d ** i <= n: i += 1

# 조건을 만족하는 d진법 d자리 수의 순열
special_val = permutations([str(i) for i in range(d)])

# n을 d진법으로 변환
val = [0 for _ in range(d)]
if i == d:
	tmp = n
	while tmp > 0:
		i -= 1
		num = 0
		digit = d ** i
		while num * digit <= tmp: num += 1
		num -= 1
		val[i] = num
		tmp -= num * digit
	val.reverse()
val = list(map(str, val))
val = int("".join(val))

# 정답 찾기
found = False
if i <= d:
	for special in special_val:
		if special[0] == '0': continue
		special = int("".join(special))
		if val < special:
			found = True
			special = list(str(special))
			special.reverse()
			val = list(map(int, special))
			break

# val을 10진법으로 다시 변환
sol = -1
if found:
	sol = 0
	for i in range(len(val)):
		sol += val[i] * (d ** i)

# output
print(sol)