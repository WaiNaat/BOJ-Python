'''
max(T)*max(K)=1,000,000이므로 무식하게 구현해도 될듯?
톱니바퀴 자체의 회전은 deque로 쉽게 가능
재귀를 이용해서 주변 톱니바퀴까지 돌릴 수 있음.
'''

import sys
from collections import deque
input = sys.stdin.readline

# function
def spin(gear, direction, clockwise):
    global T

    # 현재 3시와 9시방향 극 확인 
    left_pole = gears[gear][6]
    right_pole = gears[gear][2]

    # 회전
    if clockwise == 1:
        gears[gear].appendleft(gears[gear].pop())
    else:
        gears[gear].append(gears[gear].popleft())
    
    # 왼쪽으로
    if direction == -1 or direction is None:
        if gear > 1 and gears[gear - 1][2] != left_pole:
            spin(gear - 1, -1, -clockwise)
    
    # 오른쪽으로
    if direction == 1 or direction is None:
        if gear < T and gears[gear + 1][6] != right_pole:
            spin(gear + 1, 1, -clockwise)


# input
T = int(input())
gears = [None]
for _ in range(T):
    gear = deque(map(int, input().strip()))
    gears.append(gear)

K = int(input())
spins = [map(int, input().split()) for _ in range(K)]

# process
for gear, clockwise in spins:
    spin(gear, None, clockwise)

# output
sol = 0
for i in range(1, T + 1):
    if gears[i][0] == 1:
        sol += 1

print(sol)