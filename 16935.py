import sys
input = sys.stdin.readline

'''
(r, c)위치와 연산 x가 주어졌을 때
그 연산을 행한 결과 위치 (r2, c2)를 구해주는 함수
    >> 이거만 만들면 됨.
'''

# functions
def flip_vert(r, c, row, col, reversed):
    """1번 연산"""
    if reversed:
        row, col = col, row
    return row - 1 - r, c, reversed

def flip_horizon(r, c, row, col, reversed):
    """2번 연산"""
    if reversed:
        row, col = col, row
    return r, col - 1 - c, reversed

def rotate_clock(r, c, row, col, reversed):
    """3번 연산"""
    if reversed:
        row, col = col, row
    return c, row - 1 - r, not reversed

def rotate_anticlock(r, c, row, col, reversed):
    """4번 연산"""
    if reversed:
        row, col = col, row
    return col - 1 - c, r, not reversed

def find_quadrant(r, c, row, col):
    """(r,c)가 몇 사분면인지 찾아주는 함수"""
    row_half = row // 2
    col_half = col // 2

    if 0 <= r < row_half and 0 <= c < col_half:
        return 1
    elif 0 <= r < row_half and col_half <= c < col:
        return 2
    elif row_half <= r < row and col_half <= c < col:
        return 3
    else:
        return 4

def quadrant_clock(r, c, row, col, reversed):
    """5번 연산"""
    if reversed:
        row, col = col, row
    
    row_half = row // 2
    col_half = col // 2
    quadrant = find_quadrant(r, c, row, col)
    
    if quadrant == 1:
        return r, c + col_half, reversed
    elif quadrant == 2:
        return r + row_half, c, reversed
    elif quadrant == 3:
        return r, c - col_half, reversed
    else:
        return r - row_half, c, reversed

def quadrant_anticlock(r, c, row, col, reversed):
    """6번 연산"""
    if reversed:
        row, col = col, row
    
    row_half = row // 2
    col_half = col // 2
    quadrant = find_quadrant(r, c, row, col)

    if quadrant == 1:
        return r + row_half, c, reversed
    elif quadrant == 2:
        return r, c - col_half, reversed
    elif quadrant == 3:
        return r - row_half, c, reversed
    else:
        return r, c + col_half, reversed

# input
row, col, R = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(row)]
oper_seq = tuple(map(int, input().split()))

# process
# 정답 배열 미리 만드려면 90도 회전 횟수를 구해야 함
flag = True
for i in oper_seq:
    if i == 3 or i == 4:
        flag = not flag

# 정답 배열 생성
if flag:
    sol = [[None for _ in range(col)] for _ in range(row)]
else:
    sol = [[None for _ in range(row)] for _ in range(col)]

# 원하는 연산 mapping해주는 dict
operation = {
    1: flip_vert,
    2: flip_horizon,
    3: rotate_clock,
    4: rotate_anticlock,
    5: quadrant_clock,
    6: quadrant_anticlock
}

# 연산 실행
for r in range(row):
    for c in range(col):
        r2 = r
        c2 = c
        reversed = False # 90도 회전시 row와 col이 바뀌므로 그땐 True

        for i in oper_seq:
            r2, c2, reversed = operation[i](r2, c2, row, col, reversed)
        
        sol[r2][c2] = A[r][c]

# output
for line in sol:
    print(*line)