'''
숫자 변환에 필요한 반전 횟수를 담은 mapping table을 만들어야 함
max(N)=999,999이므로 1층~N층까지 하나씩 되는지 해보면 됨

숫자를 표현하는데 필요한 led 위치를 0과 1로 나타냄.
'''
import sys
input = sys.stdin.readline

# input
N, K, P, X = map(int, input().split())

# process
# 숫자 표현
number = [
    '1110111', '0010010', '1011101',
    '1011011', '0111010', '1101011',
    '1101111', '1010010', '1111111',
    '1111011'
]

# mapping table
change = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(i + 1, 10):
        
        cnt = 0
        for k in range(7):
            if number[i][k] != number[j][k]:
                cnt += 1

        change[i][j] = cnt
        change[j][i] = cnt

# 변환
sol = -1 # 자기 자신도 세는 경우 제외

X = tuple(map(int, str(X).zfill(K)))

for val in range(1, N + 1):
    val = tuple(map(int, str(val).zfill(K)))

    cnt = 0
    for i in range(K):
        cnt += change[X[i]][val[i]]

    if cnt <= P:
        sol += 1

# output
print(sol)