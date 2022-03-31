from collections import deque

'''
큐를 이용해서 다리 자체를 구현
단위시간 단위로 시뮬레이션
'''

# input
n, w, L = map(int, input().split())
truck = tuple(map(int, input().split()))

# process
i = 0
t = 0
weight_sum = 0
out_truck_cnt = 0
bridge = deque([0 for _ in range(w)])

while out_truck_cnt < n:

    # 트럭 1칸씩 앞으로 이동
    t += 1
    truck_weight = bridge.popleft()
    bridge.append(0)

    # 다리 빠져나온 트럭 있으면 처리
    if truck_weight != 0:
        out_truck_cnt += 1
        weight_sum -= truck_weight
    
    # 다음 트럭이 다리에 올라갈 수 있으면 올라감
    if i < n and weight_sum + truck[i] <= L:
        weight_sum += truck[i]
        bridge[-1] = truck[i]
        i += 1


# output
print(t)