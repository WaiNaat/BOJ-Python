'''
오른쪽에 있는 애들부터 오른쪽으로 옮긴다고 치면
결국 각 공 당 한 번씩만 점프하면 됨
    (본인 오른쪽에 있는애들은 이미 점프해서 뭉쳐있음)

즉 빨간색이 뛰어넘어야 하는 횟수는
(총 빨간색 개수) - (맨 오른쪽 끝에 뭉쳐있는 빨간색 개수)

같은 방법으로 파란색도 계산가능

문자열 뒤집어서 거꾸로 가는 경우도 생각
'''
# function
def move(balls):
    red_cnt = 0
    blue_cnt = 0
    prev_color = None
    cur_group_cnt = 0

    for ball in balls:
        if ball != prev_color:
            cur_group_cnt = 0
            prev_color = ball
        cur_group_cnt += 1

        if ball == 'R':
            red_cnt += 1
        else:
            blue_cnt += 1

    if balls[-1] == 'R':
        red_cnt -= cur_group_cnt
    else:
        blue_cnt -= cur_group_cnt

    return min(red_cnt, blue_cnt)

# input
N = int(input())
balls = input().rstrip()

# process & output
print(min(move(balls), move(balls[::-1])))