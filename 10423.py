'''
크루스칼 알고리즘으로 mst를 만드는 문제
단, 이미 가상의 '0번 도시'와 발전기가 설치된 도시들은 연결되어 있다고 가정
    이렇게 하면 발전소의 겹침 문제 해결 가능
'''
import sys
input = sys.stdin.readline

# functions
def union(a, b):
    a = find(a)
    b = find(b)

    if card[a] < card[b]:
        parent[a] = b
        card[b] += card[a]
    else:
        parent[b] = a
        card[a] += card[b]

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

# input
N, M, K = map(int, input().split())
power_plants = map(int, input().split())
cables = [tuple(map(int, input().split())) for _ in range(M)]

# process
parent = [i for i in range(N + 1)]
card = [1 for _ in range(N + 1)]

# 가상의 0번 도시와 발전소들 연결
for city in power_plants:
    parent[city] = 0
card[0] += K

# 크루스칼 알고리즘
cables.sort(key = lambda x: x[2])

cost = 0
edge_cnt = K

for u, v, w in cables:
    if edge_cnt == N:
        break

    if find(u) != find(v):
        union(u, v)
        cost += w
        edge_cnt += 1

# output
print(cost)