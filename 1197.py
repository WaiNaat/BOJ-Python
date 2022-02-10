import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
# function
def union(v1, v2):
	v1 = find(v1)
	v2 = find(v2)
	# 딸린 자식의 수가 작은 녀석이 큰 녀석 밑으로 들어감.
	if cardinality[v1] < cardinality[v2]:
		parent[v1] = v2
		cardinality[v2] += cardinality[v1]
	else:
		parent[v2] = v1
		cardinality[v1] += cardinality[v2]

def find(v):
	if parent[v] == 0:
		return v
	# 다음에 같은 값에 대해 더 빨리 수행하기 위해 트리 평탄화
	parent[v] = find(parent[v])
	return parent[v]

# input
v, e = map(int, input().split())
E = [tuple(map(int, input().split())) for _ in range(e)]
# process
'''
크루스칼 알고리즘 사용
parent := union-find에서 각 정점의 부모 이름을 저장
cardinality := union-find에서 각 정점별로 본인을 포함한 자식의 수를 저장
'''
parent = [0 for _ in range(v + 1)]
cardinality = [1 for _ in range(v + 1)]
E.sort(key = lambda x: x[2])
mst_edge_cnt = 0
sol = 0

for v1, v2, weight in E:
	if mst_edge_cnt == v - 1:
		break
	
	if find(v1) != find(v2):
		mst_edge_cnt += 1
		sol += weight
		union(v1, v2)
# output
print(sol)