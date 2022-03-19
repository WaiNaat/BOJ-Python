# input
n = int(input())
power = tuple(map(int, input().split()))

# process
'''
최장 부분 감소 수열의 길이를 구하는 문제.
opt(i)를 0~i번 군인들로 구성하고 본인을 마지막으로 했을 때 남은 병사의 최대 수라 하면
opt(i) = 
    1
    opt(k) + 1   (k<i이고 power(k)>power(i)인 k)
중 최댓값
'''
opt = [0 for _ in range(n)]
for i in range(n):
    for k in range(i):
        if power[k] > power[i] and opt[k] > opt[i]:
            opt[i] = opt[k]
    opt[i] += 1

# output
print(n - max(opt))