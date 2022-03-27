# input
D, K = map(int, input().split())

# process
'''
D일차 떡 개수는 mA + nB = K의 식으로 나타낼 수 있으므로
dp를 써서 D일차 떡 개수에서 m과 n값을 알 수 있음.

A, B값 찾을땐 이론상 가능한 최대 B값에서 시작,
거기부터 B값 줄여나가는 방향으로 찾으면 됨
'''
# m과 n값 구하기
coeff_A = [0 for _ in range(D + 1)]
coeff_B = [0 for _ in range(D + 1)]
coeff_A[1] = 1
coeff_B[2] = 1

for i in range(3, D + 1):
    coeff_A[i] = coeff_A[i - 1] + coeff_A[i - 2]
    coeff_B[i] = coeff_B[i - 1] + coeff_B[i - 2]

m = coeff_A[D]
n = coeff_B[D]

# A와 B값 찾기
A = 1
B = (K - m) // n + 1

while True:
    if m * A + n * B == K:
        break

    A -= 1
    if A < 1:
        B -= 1
        A = K - (n * B) // m + 1

# output
print(A)
print(B)