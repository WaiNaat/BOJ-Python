'''
남초와 여초가 번갈아 나타나야 함
    처음에 입력받을 때 남초-남초, 여초-여초 간선은 제외

크루스칼로 mst를 만들면 끝
'''

import sys
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

    if a == b: return

    if card[a] > card[b]:
        parent[b] = a
        card[a] += card[b]
    else:
        parent[a] = b
        card[b] += card[a]

# input
N, M = map(int, input().split())
gender = input().split()
E = []

for _ in range(M):
    u, v, d = map(int, input().split())
    u -= 1
    v -= 1

    if gender[u] != gender[v]:
        E.append((u, v, d))

# process
parent = [i for i in range(N)]
card = [1 for _ in range(N)]

E.sort(key = lambda x: x[2])

edge_cnt = 0
total_distance = 0

for u, v, d in E:
    if edge_cnt == N - 1:
        break

    if find(u) != find(v):
        union(u, v)
        edge_cnt += 1
        total_distance += d

# output
print(total_distance if edge_cnt == N - 1 else -1)