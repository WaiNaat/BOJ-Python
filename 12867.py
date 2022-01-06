# input
n = int(input())
m = int(input())
coord_idx = list(map(int, input().split()))
move = input()
# process
'''
수빈이가 이동한 인덱스들만 기억해야 함.(10억개 전부 말고)
dict 사용.
visited := 방문한 좌표들 목록
cur := 현재 위치
'''
visited = [{}]
cur = {}
isSuccess = True
for i in range(m):
	idx = coord_idx[i]
	val = 1 if move[i] == '+' else -1
	# 이동
	if idx not in cur: cur[idx] = 0
	cur[idx] += val
	if cur[idx] == 0: cur.pop(idx)
	# 중복인지 검사
	if cur in visited:
		isSuccess = False
		break
	else:
		visited.append(cur.copy())
# output
print(1 if isSuccess else 0)