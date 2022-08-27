'''
다익스트라
현재 방향을 유지할 경우 비용 0
방향을 바꿀 경우 비용 1
'''
import sys, heapq
input = sys.stdin.readline

# constant
INF = 12345
DIRECTIONS = ((1, 0), (0, -1), (-1, 0), (0, 1))

# input
W, H = map(int, input().split())
MAP = [input().rstrip() for _ in range(H)]

# process
h = []
mirror = [[INF for _ in range(W)] for _ in range(H)]

# 시작점 찾기
found = False
for r in range(H):
    for c in range(W):
        if MAP[r][c] == 'C':
            found = True
            mirror[r][c] = 0

            for d in range(4):
                r2 = r + DIRECTIONS[d][0]
                c2 = c + DIRECTIONS[d][1]

                if not 0 <= r2 < H or not 0 <= c2 < W or MAP[r2][c2] == '*':
                    continue

                mirror[r2][c2] = 0
                h.append((0, r2, c2, d))
            break
    if found: break


# 다익스트라
sol = None
while h:
    mirror_cnt, r, c, d = heapq.heappop(h)

    if MAP[r][c] == 'C':
        sol = mirror[r][c]
        break

    for d2 in ((d + 1) % 4, d, (d + 3) % 4):
        r2 = r + DIRECTIONS[d2][0]
        c2 = c + DIRECTIONS[d2][1]

        if not 0 <= r2 < H or not 0 <= c2 < W or MAP[r2][c2] == '*':
            continue

        next_mirror_cnt = mirror_cnt + (1 if d != d2 else 0)

        if next_mirror_cnt <= mirror[r2][c2]:
            mirror[r2][c2] = next_mirror_cnt
            heapq.heappush(h, (next_mirror_cnt, r2, c2, d2))

# output
print(sol)