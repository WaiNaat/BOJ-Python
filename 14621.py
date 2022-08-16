### 틀렸습니다 ###

'''
남초와 여초가 번갈아 나타나야 하고 한 줄로 이어져야 함 <<<<<<< 한줄이라는 소리 어디에도 없는데 왜 착각함?
    처음에 입력받을 때 남초-남초, 여초-여초 간선은 제외

크루스칼로 mst를 만들면 되는데
연결하려는 두 정점에 연결된 간선이 2개 이상이면 연결하지 않음
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
adj_univ = [0 for _ in range(N)]

for u, v, d in E:
    if edge_cnt == N - 1:
        break

    if find(u) != find(v) and adj_univ[u] < 2 and adj_univ[v] < 2:
        union(u, v)
        edge_cnt += 1
        total_distance += d
        adj_univ[u] += 1
        adj_univ[v] += 1

# output
print(total_distance if edge_cnt == N - 1 else -1)