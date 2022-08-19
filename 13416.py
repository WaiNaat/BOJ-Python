'''
크루스칼 알고리즘으로 mst 두 번 만드는 문제
'''
import sys
input = sys.stdin.readline

# functions
def union(a, b):
    a = find(a)
    b = find(b)

    if card[a] > card[b]:
        parent[b] = a
        card[a] += card[b]
    else:
        parent[a] = b
        card[b] += card[a]

def find(a):
    if parent[a] == a:
        return a

    parent[a] = find(parent[a])
    return parent[a]

def kruskal(V, E):
    uphill = 0
    edge_cnt = 0

    for A, B, C in E:
        if edge_cnt == V - 1:
            return uphill
        
        if find(A) != find(B):
            union(A, B)
            edge_cnt += 1
            uphill += 1 if not C else 0

    return uphill

# input
N, M = map(int, input().split())
E = [tuple(map(int, input().split())) for _ in range(M + 1)]

# process
# 최대 피로도 계산
E.sort(key = lambda x: x[2])

parent = [i for i in range(N + 1)]
card = [1 for _ in range(N + 1)]

max_fatigue = kruskal(N + 1, E) ** 2

# 최소 피로도 계산
E.reverse()

parent = [i for i in range(N + 1)]
card = [1 for _ in range(N + 1)]

min_fatigue = kruskal(N + 1, E) ** 2

# output
print(max_fatigue - min_fatigue)