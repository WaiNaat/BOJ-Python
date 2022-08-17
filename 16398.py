'''
크루스칼 알고리즘으로 mst 만드는 문제
인접 행렬 형태로 준걸 하나의 배열로 합쳐서 정렬해야 함
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
N = int(input())
C = [tuple(map(int, input().split())) for _ in range(N)]

# process
# 간선 배열 만들고 정렬
E = [(i, j, C[i][j]) for i in range(N) for j in range(i + 1, N)]
E.sort(key = lambda x: x[2])

# 크루스칼 알고리즘
parent = [i for i in range(N)]
card = [1 for i in range(N)]

cost = 0
edge_cnt = 0

for i, j, c in E:
    if edge_cnt == N - 1:
        break

    if find(i) != find(j):
        union(i, j)
        cost += c
        edge_cnt += 1

# output
print(cost)