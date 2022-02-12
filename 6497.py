import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
# functions
def union(v1, v2):
	v1 = find(v1)
	v2 = find(v2)
	if v1 == v2: return
	if cardi[v1] < cardi[v2]:
		cardi[v2] += cardi[v1]
		parent[v1] = v2
	else:
		cardi[v1] += cardi[v2]
		parent[v2] = v1

def find(v):
	if parent[v] != v:
		parent[v] = find(parent[v])
	return parent[v]


# input
while True:
	v, e = map(int, input().split())
	if v == 0 and e == 0: break
	street = [tuple(map(int, input().split())) for _ in range(e)]
# process
	'''
	크루스칼 알고리즘 사용
	parent := union-find에서 각 정점의 부모를 저장하는 배열
	cardi := union-find에서 각 정점을 루트로 하는 트리의 원소 수
	sol := '절약되는' 비용이므로 mst에 포함되지 않는 간선의 비용들의 합
	'''
	parent = [i for i in range(v)]
	cardi = [1 for _ in range(v)]
	street.sort(key = lambda x: x[2])
	sol = 0
	mst_edge_num = 0

	for x, y, cost in street:
		if find(x) != find(y):
			mst_edge_num += 1
			union(x, y)
		else:
			sol += cost
# output
	print(sol)