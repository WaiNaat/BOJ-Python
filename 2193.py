'''
opt(i, k) := i자리이고 k로 끝나는 이친수 개수
opt(i, 0) = opt(i-1, 0) + opt(i-1, 1)
opt(i, 1) = opt(i-1, 0)
'''
# input
n = int(input())

# process
cur_0 = 0
cur_1 = 1

for i in range(2, n + 1):
    next_0 = cur_0 + cur_1
    next_1 = cur_0

    cur_0 = next_0
    cur_1 = next_1

# output
print(cur_0 + cur_1)