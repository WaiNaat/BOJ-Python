'''
다리를 무게제한 내림차순으로 정렬
union-find로 숭이/혜빈이가 같은 트리에 연결될 때까지 다리 연결
연결되는 순간의 다리 무게제한이 답
'''
import sys
input = sys.stdin.readline

# functions
def union(a, b):
    a = find(a)
    b = find(b)

    if cardinality[a] < cardinality[b]:
        parent[a] = b
        cardinality[b] += cardinality[a]
    else:
        parent[b] = a
        cardinality[a] += cardinality[b]

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

# input
house_num, bridge_num = map(int, input().split())
start, end = map(int, input().split())
bridges = [tuple(map(int, input().split())) for _ in range(bridge_num)]

# process
bridges.sort(key = lambda x: -x[2])

parent = [i for i in range(house_num + 1)]
cardinality = [1 for _ in range(house_num + 1)]

sol = None
edge_cnt = 0

for h1, h2, k in bridges:
    if edge_cnt == house_num - 1 or find(start) == find(end):
        break

    if find(h1) != find(h2):
        union(h1, h2)
        sol = k
        edge_cnt += 1

# output
print(sol if find(start) == find(end) else 0)