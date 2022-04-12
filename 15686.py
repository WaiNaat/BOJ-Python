'''
입력받으면서 치킨집과 집 좌표 따로 저장
조합으로 M개 뽑아서 치킨거리 계산
'''
from itertools import combinations
# function
def calc_min_chicken_dist(house, chicken):
    ret = 1234

    for c in chicken:
        dist = abs(house[0] - c[0]) + abs(house[1] - c[1])
        ret = min(ret, dist)

    return ret

# input
N, M = map(int, input().split())
chicken = []
house = []
for i in range(N):
    line = tuple(map(int, input().split()))
    
    for j in range(N):
        if line[j] == 1:
            house.append((i, j))
        elif line[j] == 2:
            chicken.append((i, j))

# process
sol = 12345678
for c in combinations(chicken, M):
    dist = 0
    for h in house:
        dist += calc_min_chicken_dist(h, c)
    sol = min(sol, dist)

# output
print(sol)