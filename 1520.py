### 시간 초과 ###

'''
dfs로 길찾기
'''
import sys
input = sys.stdin.readline

# input
row, col = map(int, input().split())
height = [tuple(map(int, input().split())) for _ in range(row)]

# process
stack = [(0, 0, height[0][0])]
sol = 0
directions = ((-1, 0), (1, 0), (0, 1), (0, -1))

while stack:
    r, c, h = stack.pop()

    if r == row - 1 and c == col - 1:
        sol += 1
        continue

    for dr, dc in directions:
        r2 = r + dr
        c2 = c + dc

        if not 0 <= r2 < row or not 0 <= c2 < col:
            continue

        if height[r2][c2] < h:
            stack.append((r2, c2, height[r2][c2]))

# output
print(sol)