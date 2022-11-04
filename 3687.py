'''
가장 큰 수 찾기: 그리디
가장 작은 수 찾기: DP

수가 커지려면 자릿수가 커지는게 장땡임
가장 성냥개비를 적게 먹는게(2개) '1' 이므로 여기에 전부 투자.
홀수로 남을 경우 가장 큰 자리에 성냥개비를 가장 작은 홀수개(3개) 먹는 '7'을 쓴다.

일단 같은 개수의 성냥개비로는 최대한 작은 수를 만들어야함 (5개로는 2, 3, 5를 만들수있는데 2만 만들어야함)
opt(i) := i개로 만들 수 있는 최소숫자
make(i) := i개로 만들 수 있는 최소숫자. 단, 2 <= i <= 7
opt(i) = min(opt(i-k) 앞 또는 뒤에 k개로 만들 수 있는 최소숫자를 붙인 것), 2 <= k <= 7

수기로 개수-숫자 mapping table 적고 시작
'''
import sys
input = sys.stdin.readline

# function
def calc_max(n):
    if n % 2 == 0:
        return '1' * (n // 2)
    
    return ''.join(['7', '1' * ((n - 3) // 2)])
    
# input & process
num_tests = int(input())
sol = []
opt = [None, None, 1, 7, 4, 2, 6, 8]
min_table = [None, None, 1, 7, 4, 2, 0, 8]

for _ in range(num_tests):
    n = int(input())

    for i in range(len(opt), n + 1):
        val = float('inf')
        for k in range(2, 8):
            if i - k < 2: break
            val = min(
                opt[i - k] * 10 + min_table[k],
                int(''.join([str(opt[k]), str(opt[i - k])])),
                val
            )
        opt.append(val)

    sol.append(f'{opt[n]} {calc_max(n)}')

# output
print('\n'.join(sol))