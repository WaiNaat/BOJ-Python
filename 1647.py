import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# functions
def union(v1, v2):
	v1 = find(v1)
	v2 = find(v2)

	small = v1 if card[v1] < card[v2] else v2
	big = v2 if card[v1] < card[v2] else v1

	parent[small] = big
	card[big] += card[small]

def find(v):
	if parent[v] == v:
		return v
	
	parent[v] = find(parent[v])
	return parent[v]

# input
n, m = map(int, input().split())
road = [tuple(map(int, input().split())) for _ in range(m)]

# process
'''
크루스칼 알고리즘 사용.
근데 한 마을을 두 집단으로 나눠야 함.
>> mst 만들기에서 맨 마지막 간선을 추가하지 않으면 됨.

parent := union-find에서 각 정점별로 부모를 저장하는 배열
card := union-find에서 정점별로 본인을 포함한 자식 수를 저장하는 배열
mst_edge_cnt := 현재 mst에 포함된 간선 수
'''
parent = [i for i in range(n + 1)]
card = [1 for _ in range(n + 1)]
mst_edge_cnt = 0
sol = 0

road.sort(key = lambda x: x[2])

for a, b, c in road:
	if mst_edge_cnt == n - 2:
		break

	if find(a) != find(b):
		mst_edge_cnt += 1
		sol += c
		union(a, b)

# output
print(sol)