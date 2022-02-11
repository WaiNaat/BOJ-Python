import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
from math import sqrt
# functions
distance = lambda a, b: sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))

def union(v1, v2):
	v1 = find(v1)
	v2 = find(v2)
	if v1 == v2: return
	# cardinality가 더 작은 트리가 더 큰 트리 밑으로 들어감
	if card[v1] < card[v2]:
		parent[v1] = v2
		card[v2] += card[v1]
	else:
		parent[v2] = v1
		card[v1] += card[v2]

def find(v):
	if parent[v] == v:
		return v
	# 부모 찾으면서 트리 평탄화 작업도 실행
	parent[v] = find(parent[v])
	return parent[v]


# input
n = int(input())
V = []
E = []

for i in range(n):
	V.append(tuple(map(float, input().split())))
	for j in range(i):
		E.append((distance(V[i], V[j]), i, j))

# process
'''
별 입력 받을 때마다 모든 별돌과 거리 계산해서 간선으로 반영.
크루스칼 알고리즘 사용
parent := union find에서 각 정점의 부모 정점을 저장하는 배열
card := union find에서 각 정점의 자신을 포함한 자식의 수를 저장하는 배열(cardinality)
'''
E.sort(key = lambda x: x[0])
parent = [i for i in range(n)]
card = [1 for _ in range(n)]
sol = 0
mst_edge_cnt = 0

for d, v1, v2 in E:
	if mst_edge_cnt == n - 1:
		break

	if find(v1) != find(v2):
		sol += d
		mst_edge_cnt += 1
		union(v1, v2)

# output
print(sol)