import sys
input = sys.stdin.readline

# functions
def DFS(trash):
	stack = [trash]
	cnt = 1
	visited[trash] = 1

	while stack:
		trash = stack.pop()
		for adj in hallway[trash]:
			if visited[adj] == 0:
				visited[adj] = 1
				cnt += 1
				stack.append(adj)
	return cnt

# input
height, width, K = map(int, input().split())
hallway = {}
'''
음식물 쓰레기 좌표를 XXXYYY의 여섯 자리 숫자로 변환 (x좌표와 y좌표는 0~99사이라서 가능)
딕셔너리를 이용해 인접 리스트 저장
'''
for _ in range(K):
	y, x = map(int, input().split())
	trash = 1000 * x + y
	if trash not in hallway: hallway[trash] = set([])

	# 상하좌우 확인
	directions = (1000, -1000, 1, -1)
	for move in directions:
		adj = trash + move
		if adj in hallway:
			hallway[trash].add(adj)
			hallway[adj].add(trash)
	
# process
visited = {trash:0 for trash in hallway.keys()}
max_size = 0
for trash in hallway.keys():
	if visited[trash] == 0:
		size = DFS(trash)
		if max_size < size: max_size = size

# output
print(max_size)