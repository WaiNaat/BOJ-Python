# input
n = int(input())
# process
'''
소수 목록을 만든다.
연속된 두 소수를 곱해 특별한 수 목록을 만든다.
max(N)=100*100이므로 100보다 큰 두 소수까지만 필요함.
'''
not_prime = set([])
prime = []
for i in range(2, 110):
	if i not in not_prime:
		prime.append(i)
		val = i
		while val < 110:
			not_prime.add(val)
			val += i
special_num = []
for i in range(1, len(prime)):
	special_num.append(prime[i] * prime[i-1])
sol = -1
for i in special_num:
	if i > n:
		sol = i
		break
# output
print(sol)