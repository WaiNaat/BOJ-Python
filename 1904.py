# input
n = int(input())
# process
'''
길이가 n인 수열 만들기
	n-2길이인 수열 뒤에 '00' 붙이기
	n-1길이인 수열 뒤에 '1' 붙이기
1
00 11
100 001 111
1001 0011 1111 0000 1100
즉 opt(n) = opt(n-2) + opt(n-1)
opt(1)=1, opt(2)=2

나머지 연산에서
A = B + C일 때 A%x = (B%x + C%x) % x
'''
opt = [0, 1, 2]
for i in range(3, n + 1):
	opt_i = (opt[i - 2] + opt[i - 1]) % 15746
	opt.append(opt_i)
# output
print(opt[n])