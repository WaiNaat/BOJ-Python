### 안돌려봤는데 시간초과나 메모리초과날듯 ###

'''
opt(jump) := jump번 뛰어서 도착할 수 있는 위치들의 집합. (현위치, 마지막 점프길이)
'''
import sys
input = sys.stdin.readline

# input
N, M = map(int, input().split())
small_stones = set([int(input()) for _ in range(M)])

# process
cur = {(1, 0)}
found = False
sol = float('inf')

for jump in range(1, N):
    next = set()
    for stone, jump_length in cur:
        for k in (-1, 0, 1):
            next_stone = stone + jump_length + k
            
            if next_stone == N:
                found = True
                sol = jump
                break

            if not 0 < next_stone < N:
                continue

            next.add((next_stone, jump_length + k))

    if found: break
    cur = next


# output
print(sol if found else -1)