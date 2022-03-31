### 틀렸습니다 ###

from collections import deque

'''
큐를 이용해서 각 트럭이 다리를 벗어나는 시간을 기억,
다리 무게가 꽉 찼을 경우
바로 맨 앞 트럭이 다리를 벗어날 때의 시간으로 이동
'''

# input
n, w, L = map(int, input().split())
truck = tuple(map(int, input().split()))

# process
i = 0
t = 1
weight_sum = 0
bridge = deque()

while i < n:

    # 트럭을 다리 위에 올릴 수 있으면 올림
    if len(bridge) < n and weight_sum + truck[i] <= L:
        weight_sum += truck[i]
        bridge.append((truck[i], t + w))
        i += 1
        t += 1
    
    # 다리 무게가 꽉 찼을 경우 다리의 맨 앞 트럭 제거
    else:
        truck_weight, time = bridge.popleft()
        weight_sum -= truck_weight
        t = time

# 다리의 마지막 트럭이 빠져나오는 시간
_, time = bridge.pop()
t = time

# output
print(t)