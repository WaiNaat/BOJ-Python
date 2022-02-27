import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# functions
def union(v1, v2):
	v1 = find(v1)
	v2 = find(v2)
	if v1 == v2: return

	large, small = (v1, v2) if card[v1] > card[v2] else (v2, v1)
	card[large] += card[small]
	parent[small] = large

def find(v):
	if parent[v] == v:
		return v

	parent[v] = find(parent[v])
	return parent[v]

# input
n = int(input())
m = int(input())
E = [tuple(map(int, input().split())) for _ in range(m)]

# process
'''
모든 컴퓨터 연결, 연결비용 최소
>> mst: 크루스칼 알고리즘 사용.

parent := union-find에서 각 정점의 부모 저장하는 배열
card := union-find에서 각 정점별로 본인을 포함한 자식 수를 저장하는 배열
cost := 문제에서 요구하는 비용
mst_edge_cnt := mst에 포함된 간선 수
'''
parent = [i for i in range(n + 1)]
card = [1 for _ in range(n + 1)]
cost = mst_edge_cnt = 0

E.sort(key = lambda x: x[2])
for a, b, c in E:
	if mst_edge_cnt == n - 1:
		break
	if find(a) != find(b):
		mst_edge_cnt += 1
		cost += c
		union(a, b)

# output
print(cost)