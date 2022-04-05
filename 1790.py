'''
1 ~ 1 + (10-0)*1 - 1 : 한 자리 숫자
10 ~ 10 + (100-10)*2 - 1 : 두 자리 숫자
190 ~ 190 + (1000-100)*3 - 1 : 세 자리 숫자
이런 방식으로
k위치의 값이 몇 자리 숫자의 일부인지 알 수 있음.

k가 `digits`자리 숫자, x자리 숫자의 시작 index를 `idx`라 하면
(k-idx)/digits로 k가 정확히 어떤 숫자의 일부인지 구할 수 있음.
'''

# input
N, k = map(int, input().split())

# process
# 변수 초기화
digits = 1
idx = 1

# k 위치의 값이 몇 자리 숫자의 일부인지 계산
if k > 9:
    while idx + (10 ** digits - 10 ** (digits - 1)) * digits < k:
        idx += (10 ** digits - 10 ** (digits - 1)) * digits
        digits += 1

# k가 정확히 어떤 숫자의 일부인지 계산
val, mod = divmod(k - idx, digits)
val += 10 ** (digits - 1)
sol = str(val)[mod]

# output
print(sol if val <= N else -1)