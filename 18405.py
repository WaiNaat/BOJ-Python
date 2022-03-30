import sys
input = sys.stdin.readline
'''
BFS를 쓰면 초 단위로 바이러스 퍼지는거 파악 가능
각 바이러스별로 다음 단위시간에 퍼질 구역들을 저장할 배열 필요.
'''
# function
def spread(virus, queue, N):
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    next = []

    while queue:
        r, c = queue.pop()

        for dr, dc in directions:
            r2 = r + dr
            c2 = c + dc

            if not 0 <= r2 < N or not 0 <= c2 < N:
                continue

            if test_tube[r2][c2] == 0:
                test_tube[r2][c2] = virus
                next.append((r2, c2))

    return next

# input
N, K = map(int, input().split())
test_tube = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

# process
# 바이러스 초기 위치 저장
virus_next = [[] for _ in range(K + 1)]
for r in range(N):
    for c in range(N):
        if test_tube[r][c] != 0:
            virus_next[test_tube[r][c]].append((r, c))

# 바이러스 확산
while S > 0:
    for i in range(1, K + 1):
        virus_next[i] = spread(i, virus_next[i], N)
    S -= 1

# output
print(test_tube[X - 1][Y - 1])