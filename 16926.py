import sys
input = sys.stdin.readline

# functions
def get_square(r, c, row, col):
    '''
    주어진 좌표가 어떤 사각형에 위치해 있는지 계산
    반환값은 해당 사각형의 시작행번호, 시작열번호, 끝행번호, 끝열번호.
    '''
    row -= 1
    col -= 1
    i = 0

    while True:
        if ((r == i or r == row) and i <= c <= col) \
            or ((c == i or c == col) and i <= r <= row):
            return i, i, row, col
        
        i += 1
        row -= 1
        col -= 1

def rotate(r, c, row, col, R):
    '''A[r][c]를 R번 회전시켰을 때 이동되는 좌표 반환'''
    start_row, start_col, end_row, end_col = get_square(r, c, row, col)
    rotation_left = R

    # 혹시 R값이 커서 사각형을 여러 바퀴 돌아야 할 경우 제거
    rotation_length = 2 * (end_row - start_row + end_col - start_col)
    rotation_left %= rotation_length

    # 회전
    while rotation_left > 0:

        # 좌상단 -> 좌하단 이동
        if start_row <= r < end_row and c == start_col:
            if rotation_left >= end_row - r:
                rotation_left -= end_row - r
                r = end_row
            else:
                r += rotation_left
                rotation_left = 0
        
        # 좌하단 -> 우하단 이동
        elif r == end_row and start_col <= c < end_col:
            if rotation_left >= end_col - c:
                rotation_left -= end_col - c
                c = end_col
            else:
                c += rotation_left
                rotation_left = 0

        # 우하단 -> 우상단 이동
        elif start_row < r <= end_row and c == end_col:
            if rotation_left >= r - start_row:
                rotation_left -= r - start_row
                r = start_row
            else:
                r -= rotation_left
                rotation_left = 0

        # 우상단 -> 좌상단 이동
        elif r == start_row and start_col < c <= end_col:
            if rotation_left >= c - start_col:
                rotation_left -= c - start_col
                c = start_col
            else:
                c -= rotation_left
                rotation_left = 0
    
    return r, c
            
# input
row, col, R = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(row)]

# process
'''
A[r][c]의 값을 R번 돌렸을 때
최종 위치 A[r2][c2]를 계산해주는 함수만 만들면 됨
'''
sol = [[None for _ in range(col)] for _ in range(row)]

for r in range(row):
    for c in range(col):
        r2, c2 = rotate(r, c, row, col, R)
        sol[r2][c2] = A[r][c]

# output
for line in sol:
    print(*line)