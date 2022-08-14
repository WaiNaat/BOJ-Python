'''
크루스칼 알고리즘을 써서 mst 만드는 문제.
모든 우주신들에게 서로가 서로를 연결하는 간선 부여
    단 이미 연결된 간선은 길이 0으로 취급
'''

import sys
from math import sqrt
input = sys.stdin.readline

# functions
def find(a):
    if parent[a] == a:
        return a

    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if (a == b): return

    if cardinality[a] < cardinality[b]:
        parent[a] = b
        cardinality[b] += cardinality[a]
    else:
        parent[b] = a
        cardinality[a] += cardinality[b]

# input
N, M = map(int, input().split())
gods = [tuple(map(int, input().split())) for _ in range(N)]
edges = []
for _ in range(M):
    a, b = map(int, input().split())
    edges.append((a - 1, b - 1, 0))

# process
# 나머지 간선 생성
for i in range(N):
    for j in range(i, N):
        d = sqrt((gods[i][0] - gods[j][0]) ** 2 + (gods[i][1] - gods[j][1]) ** 2)
        edges.append((i, j, d))

# 크루스칼 알고리즘 사용
parent = [i for i in range(N)]
cardinality = [0 for _ in range(N)]

edges.sort(key = lambda x: x[2])

mst_edge_cnt = 0
min_length = 0

for a, b, d in edges:
    if mst_edge_cnt == N - 1:
        break

    if find(a) != find(b):
        union(a, b)
        mst_edge_cnt += 1
        min_length += d

# output
print(f'{min_length:.2f}')