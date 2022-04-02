import sys
input = sys.stdin.readline

'''
칸 수는 최대 4만 개, max(N)=200이니까
8,000,000회 반복에 한 칸당 주변 4칸 확인하니까
대략 3200만 회 << 완전탐색 가능할듯?

초 단위로 시뮬레이션 만들면 되고
격자판에 각 폭탄이 설치된 시간을 저장하면 된다.   
'''

# function
def boom(t, r, c, row, col):
    """t-3시간에 설치된 폭탄이 (r,c)에 있으면 터뜨림"""
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    if grid[r][c] == t - 3:
        grid[r][c] = -1

        for dr, dc in directions:
            r2 = r + dr
            c2 = c + dc

            if not 0 <= r2 < row or not 0 <= c2 < col:
                continue

            # 만약 주변의 폭탄도 t시간에 터지는 거였으면
            # 동시에 터지기 때문에 얘는 처리하지 않음
            if grid[r2][c2] != t - 3:
                grid[r2][c2] = -1

# input
row, col, N = map(int, input().split())
grid = []
for _ in range(row):
    line = list(input().rstrip())

    for i in range(col):
        if line[i] == '.':
            line[i] = -1
        else:
            line[i] = 0

    grid.append(line)

# process
t = 1
while t < N:
    t += 1

    # 폭탄을 설치함
    if t % 2 == 0:
        for r in range(row):
            for c in range(col):
                if grid[r][c] == -1:
                    grid[r][c] = t

    # 폭탄이 터짐
    else:
        for r in range(row):
            for c in range(col):
                boom(t, r, c, row, col)

# output
for r in range(row):
    for c in range(col):
        print('.' if grid[r][c] == -1 else 'O', end='')
    print()