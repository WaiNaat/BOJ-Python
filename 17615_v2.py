### 이게 좀더 느림 ###

'''
오른쪽에 있는 애들부터 오른쪽으로 옮긴다고 치면
결국 각 공 당 한 번씩만 점프하면 됨
    (본인 오른쪽에 있는애들은 이미 점프해서 뭉쳐있음)

즉 빨간색이 뛰어넘어야 하는 횟수는
(총 빨간색 개수) - (맨 오른쪽 끝에 뭉쳐있는 빨간색 개수)

같은 방법으로 파란색도 계산가능

공을 왼쪽으로 뭉칠수도 있으니까 왼쪽 끝에 뭉쳐있는 애들 개수도 세는게 좋음
'''    
# input
N = int(input())
balls = input().rstrip()

# process
red_cnt = 0
blue_cnt = 0
prev_color = balls[0]
last_group_cnt = 0
first_group_cnt = 0
is_first_group = True

for ball in balls:
    if ball != prev_color:
        is_first_group = False
        last_group_cnt = 0
        prev_color = ball
    
    if is_first_group: first_group_cnt += 1
    last_group_cnt += 1

    if ball == 'R':
        red_cnt += 1
    else:
        blue_cnt += 1

sol = 1234567
if balls[-1] == 'R':
    sol = min(red_cnt - last_group_cnt, blue_cnt, sol)
else:
    sol = min(red_cnt, blue_cnt - last_group_cnt, sol)

if balls[0] == 'R':
    sol = min(red_cnt - first_group_cnt, blue_cnt, sol)
else:
    sol = min(red_cnt, blue_cnt - first_group_cnt, sol)

# output
print(sol)