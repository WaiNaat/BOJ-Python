'''
들어간 차 목록 큐 enter
나온 차 목록 큐 leave

enter 맨 앞의 차가 이미 나왔으면
    enter 맨 앞의 차 제거
enter 맨 앞의 차 = leave 맨 앞의 차면
    추월 아님
아니면
    추월한거임
'''

from collections import deque
import sys
input = sys.stdin.readline

# input
N = int(input())
enter = deque([input().rstrip() for _ in range(N)])
leave = deque([input().rstrip() for _ in range(N)])

# process
sol = 0
left_car_names = set()

while leave:

    while enter and enter[0] in left_car_names:
        enter.popleft()
    
    if enter[0] == leave[0]:
        enter.popleft()
        left_car_names.add(leave.popleft())
    else:
        sol += 1
        left_car_names.add(leave.popleft())

# output
print(sol)