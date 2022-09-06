'''
bfs를 이용해 길을 지나가지 않고 만나는 소들의 수를 세면
반대로 길을 지나가야만 만날 수 있는 소의 수를 알 수 있다.
'''
import sys
from collections import deque
input = sys.stdin.readline

# constant
directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

# function
def bfs(N, r, c):
    visited = [[False for _ in range(N)] for _ in range(N)]
    q = deque([(r, c)])
    cow_cnt = 0

    while q:
        r, c = q.popleft()

        if visited[r][c]: continue
        visited[r][c] = True

        if (r, c) in cows:
            cow_cnt += 1

        for dr, dc in directions:
            r2 = r + dr
            c2 = c + dc

            if not 0 <= r2 < N or not 0 <= c2 < N or visited[r2][c2]:
                continue

            if (r, c) not in road or (r2, c2) not in road[(r, c)]:
                q.append((r2, c2))
    
    return cow_cnt

# input
N, K, R = map(int, input().split())
road = {}
for _ in range(R):
    r1, c1, r2, c2 = map(lambda x: int(x) - 1, input().split())
    if (r1, c1) not in road:
        road[(r1, c1)] = set()
    if (r2, c2) not in road:
        road[(r2, c2)] = set()

    road[(r1, c1)].add((r2, c2))
    road[(r2, c2)].add((r1, c1))
cows = set([tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(K)])

# process
cnt = 0
for r, c in cows:
    cnt += len(cows) - bfs(N, r, c)
cnt /= 2

# output
print(int(cnt))