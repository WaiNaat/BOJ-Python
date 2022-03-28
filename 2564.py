import sys
input = sys.stdin.readline

'''
일단 시계로 돌든 반시계로 돌든 하나만 해보면 나머지 거리는 알 수 있음

그냥 배열 만들고 거기에 상점들 넣고
동근이 위치부터 시계방향으로 한바퀴 쭉 돌면서 계산
'''

# input
col, row = map(int, input().split())
store_num = int(input())

block = [[False for _ in range(col + 1)] for _ in range(row + 1)]
for _ in range(store_num):
    dir, dist = map(int, input().split())

    if dir == 1:
        block[0][dist] = True
    elif dir == 2:
        block[row][dist] = True
    elif dir == 3:
        block[dist][0] = True
    else:
        block[dist][col] = True

cur_row = None
cur_col = None
dir, dist = map(int, input().split())
if dir == 1:
    cur_row = 0
    cur_col = dist
elif dir == 2:
    cur_row = row
    cur_col = dist
elif dir == 3:
    cur_row = dist
    cur_col = 0
else:
    cur_row = dist
    cur_col = col

# process
sol = 0
perimeter = 2 * (row + col)
dist = 0

while store_num > 0:

    # 상점이 있으면 거리 반영
    if block[cur_row][cur_col]:
        sol += min(dist, perimeter - dist)
        store_num -= 1

    # 북쪽
    if cur_row == 0 and cur_col < col:
        cur_col += 1

    # 남쪽
    elif cur_row == row and cur_col > 0:
        cur_col -= 1

    # 서쪽
    elif cur_col == 0 and cur_row > 0:
        cur_row -= 1

    # 동쪽
    elif cur_col == col and cur_row < row:
        cur_row += 1

    dist += 1

# output
print(sol)