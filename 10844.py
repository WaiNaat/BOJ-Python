# input
n = int(input())
# process
'''
길이가 i이고 일의 자리 숫자가 k인 계단 수의 개수를 opt(i, k)라 하면
opt(i, 0) = opt(i-1, 1)
opt(i, 1) = opt(i-1, 0) + opt(i-1, 2)
 ...
opt(i, 9) = opt(i-1, 8)
이런 식으로 점화식을 세울 수 있다.

calc_stair_num(stair, k) := 일의 자리 숫자가 k인 계단 수의 개수 반환.
ith_stair_num[k] := 길이가 i이고 일의 자리 숫자가 k인 계단 수의 개수
'''
calc_stair_num = lambda stair, k: stair[1] if k == 0 else stair[8] if k == 9 else stair[k - 1] + stair[k + 1]
ith_stair_num = [1 for _ in range(10)]
ith_stair_num[0] = 0
for _ in range(2, n + 1):
	ith_stair_num = [calc_stair_num(ith_stair_num, k) for k in range(10)]
# output
print(sum(ith_stair_num) % 1000000000)