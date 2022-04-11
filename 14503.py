'''
문제에서 주어진 작동 순서대로 그냥 작동하면 된다.
방향은 dict로 만들면 좌회전과 후진이 쉽다.
'''

import sys
input = sys.stdin.readline

# input
row, col = map(int, input().split())
r, c, d = map(int, input().split())
place = [list(input().split()) for _ in range(row)]

# process
# 초기화
stop = False
cnt = 0
direction = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)
}

# 청소기 작동
while not stop:

    rotateCnt = 0

    # 현재 위치 청소
    if place[r][c] == '0':
        cnt += 1
        place[r][c] = '2'
    
    while rotateCnt < 4:
        # 왼쪽 확인
        dr, dc = direction[(d - 1) % 4]
        r2 = r + dr
        c2 = c + dc

        # 왼쪽으로 회전
        d = (d - 1) % 4
        rotateCnt += 1

        # 이동
        if place[r2][c2] == '0':
            r, c = r2, c2
            rotateCnt = 0
            break

    # 후진
    if rotateCnt == 4:
        # 뒤쪽 확인
        dr, dc = direction[(d - 2) % 4]
        r2 = r + dr
        c2 = c + dc

        if place[r2][c2] == '1':
            stop = True
        
        else:
            r, c = r2, c2

# output
print(cnt)