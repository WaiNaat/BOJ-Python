import sys
input = sys.stdin.readline

'''
최대 학생 수는 400명이니까
완전탐색 하면 대략 16만 회 << 가능할듯?

학생 번호가 주어졌을 때 조건에 맞는 자리 찾아주는 함수 필요
'''

# functions
def find_seat(student, like, N):
    """classroom 배열에 학생 배치"""
    seat_pos = (-1, -1)
    seat_adj_like = -1
    seat_adj_empty = -1

    for r in range(N):
        for c in range(N):
            if classroom[r][c] != 0:
                continue

            like_cnt, empty_cnt = look_around(r, c, N, like)

            # 1번 조건 비교
            if like_cnt > seat_adj_like:
                seat_pos = (r, c)
                seat_adj_like = like_cnt
                seat_adj_empty = empty_cnt
            
            # 2번 조건 비교
            elif like_cnt == seat_adj_like \
                and empty_cnt > seat_adj_empty:
                seat_pos = (r, c)
                seat_adj_empty = empty_cnt
            
            # 3번 조건은 for문 탐색순서 덕분에 자동 해결

    r, c = seat_pos
    classroom[r][c] = student

def look_around(row, col, N, like):
    """인접 자리를 둘러보고 좋아하는 학생 수 반환"""
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
    like_cnt = 0
    empty_cnt = 0

    for dr, dc in directions:
        r = row + dr
        c = col + dc

        if not 0 <= r < N or not 0 <= c < N:
            continue

        if classroom[r][c] == 0:
            empty_cnt += 1
        elif classroom[r][c] in like:
            like_cnt += 1
    
    return (like_cnt, empty_cnt)


# input
N = int(input())
student_order = []
student_info = {}
for _ in range(N ** 2):
    a, b, c, d, e = map(int, input().split())
    student_order.append(a)
    student_info[a] = (b, c, d, e)

# process
classroom = [[0 for _ in range(N)] for _ in range(N)]

# 학생 배치
for s in student_order:
    like = student_info[s]
    find_seat(s, like, N)

# 만족도 계산
sol = 0
score_table = [0, 1, 10, 100, 1000]
for r in range(N):
    for c in range(N):
        like = student_info[classroom[r][c]]
        sol += score_table[look_around(r, c, N, like)[0]]

# output
print(sol)