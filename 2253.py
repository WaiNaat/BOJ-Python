### 메모리 초과 ###

'''
opt(cur, jump) := jump칸만큼 뛰어서 cur에 도착하는 데 필요한 최소 점프 수
opt(cur, jump)에 도달하려면 cur-jump에서 출발해야 하고 이전 점프길이가 jump-1, jump, jump+1이어야 함
opt(cur, jump) = 
    opt(cur-jump, jump+k)
    k는 -1, 0, 1중 하나
    이 값들 중 최솟값 + 1
'''
import sys
input = sys.stdin.readline

# input
N, M = map(int, input().split())
small_stones = set([int(input()) for _ in range(M)])

# process
opt = [[float('inf') for _ in range(N + 1)] for _ in range(N + 1)]
opt[1][0] = 0

for stone in range(2, N + 1):
    if stone in small_stones: continue

    for jump in range(1, min(stone + 1, N)):
        if not 0 < stone - jump <= N: continue

        opt[stone][jump] = 1 + min(
            opt[stone - jump][jump - 1],
            opt[stone - jump][jump],
            opt[stone - jump][jump + 1]
        )
                
# output
val = min(opt[N])
print(val if val != float('inf') else -1)