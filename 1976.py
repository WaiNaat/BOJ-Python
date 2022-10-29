'''
union-find로 그래프를 정리
만약 find(a)=find(b)면 어떻게든 여행이 가능함
아니면 애초에 갈수있는 방법자체가 없어서 불가
'''
import sys
input = sys.stdin.readline

# functions
def union(a, b):
    parent[find(b)] = find(a)

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

# input
N = int(input())
M = input()
adj_matrix = [tuple(map(int, input().split())) for _ in range(N)]
travel_list = tuple(map(lambda x: int(x) - 1, input().split()))

# process
parent = [i for i in range(N)]

for i in range(N):
    for j in range(i+1, N):
        if adj_matrix[i][j] == 1 and find(i) != find(j):
            union(i, j)

can_travel = True
base = find(travel_list[0])
for city in travel_list:
    if find(city) != base:
        can_travel = False
        break

# output
print('YES' if can_travel else 'NO')