'''
opt(cur, jump) := jump칸만큼 뛰어서 cur에 도착하는 데 필요한 최소 점프 수
opt(cur, jump)에 도달하려면 cur-jump에서 출발해야 하고 이전 점프길이가 jump-1, jump, jump+1이어야 함
opt(cur, jump) = 
    opt(cur-jump, jump+k)
    k는 -1, 0, 1중 하나
    이 값들 중 최솟값 + 1

jump range 설정
계속 속도가 증가한다고 할때 x(x+1)/2>N 인 x번 점프하면 도착가능하고 이때 속도는 x
대충 N*2 ** 0.5 + 2정도 해주면 될듯?
'''
import sys
input = sys.stdin.readline

# input
N, M = map(int, input().split())
small_stones = set([int(input()) for _ in range(M)])

# process
jump_range = int((N * 2) ** 0.5 + 2)
opt = [[float('inf') for _ in range(jump_range + 1)] for _ in range(N + 1)]
opt[1][0] = 0

for stone in range(2, N + 1):
    if stone in small_stones: continue

    for jump in range(1, jump_range):
        if not 0 < stone - jump <= N: continue

        opt[stone][jump] = 1 + min(
            opt[stone - jump][jump - 1],
            opt[stone - jump][jump],
            opt[stone - jump][jump + 1]
        )
                
# output
val = min(opt[N])
print(val if val != float('inf') else -1)