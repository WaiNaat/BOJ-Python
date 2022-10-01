'''
냅색 문제
    가방의 크기: 비용
    물건의 가치: 용량
    물건: 앱

opt(i, j) := 0번~i번 앱에서 j비용을 맞춰서 종료했을 때 얻는 최대 용량
opt(i, j) = 
    opt(i-1, j)   (i번 앱을 종료하지 않음)
    opt(i-1, j-c[i]) + m[i]   (i번 앱을 종료함)
    둘 중 큰 값.

opt(i, ?) 계산엔 opt(i-1, ?)값들만 쓰니까 prev, cur 두개만 사용
'''
import sys
input = sys.stdin.readline

# input
N, M = map(int, input().split())
m = list(map(int, input().split()))
c = list(map(int, input().split()))

# process
MAX_COST = sum(c)

prev = [0 for _ in range(MAX_COST + 1)]
for i in range(N):
    cur = [0 for _ in range(MAX_COST + 1)]
    for j in range(MAX_COST + 1):
        cur[j] = max(prev[j], prev[j - c[i]] + m[i] if j - c[i] >= 0 else 0)
    prev = cur

sol = None
for i in range(MAX_COST + 1):
    if prev[i] >= M:
        sol = i
        break

# output
print(sol)