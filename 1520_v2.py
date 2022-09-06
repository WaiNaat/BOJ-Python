'''
opt(i, j) := (i, j)까지 오는 경우의 수
opt(i, j) := 본인 주변 4칸 중 본인보다 높은 친구들의 opt값들의 합

핵심은 opt배열을 채우는 순서
>> 높은 순서대로 처리
'''
import sys
input = sys.stdin.readline

# input
row, col = map(int, input().split())
height = [tuple(map(int, input().split())) for _ in range(row)]

# process
height_list = [(height[i][j], i, j) for i in range(row) for j in range(col)]
opt = [[0 for _ in range(col)] for _ in range(row)]
directions = ((-1, 0), (0, -1), (1, 0), (0, 1))

opt[0][0] = 1

height_list.sort(key = lambda x: -x[0])

for h, r, c in height_list:
    for dr, dc in directions:
        r2 = r + dr
        c2 = c + dc

        if not 0 <= r2 < row or not 0 <= c2 < col:
            continue

        if height[r2][c2] > h:
            opt[r][c] += opt[r2][c2]

    if r == row - 1 and c == col - 1:
        break

# output
print(opt[row - 1][col - 1])