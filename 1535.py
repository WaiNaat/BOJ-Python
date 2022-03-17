# input
n = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

# process
'''
배낭 채우기 문제.
체력 i일때 0~j번 사람들에게 인사했을 때 얻는 최대 기쁨을 opt(i, j)라 하면
opt(i, j) = 
    opt(i, j-1)    (j번 사람에게 인사하지 않음)
    opt(i-L(j), j-1) + J(j)   (j번 사람에게 인사함)
둘 중 큰 값.

점화식에 사용되는 j값은 j, j-1 두 개이므로
prev := opt(i, j-1)의 배열
cur := opt(i, j)의 배열
로 바꿔서 사용.
'''
prev = [0 for _ in range(101)]

for j in range(n):
    cur = prev.copy()

    for i in range(1, 101):
        if i - L[j] > 0:
            cur[i] = max(prev[i], prev[i - L[j]] + J[j])

    prev = cur

# output
print(prev[-1])