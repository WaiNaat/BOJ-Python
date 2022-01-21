import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# function
def canFold(paper):
	'''
	가운데를 기준으로 종이를 왼쪽과 오른쪽으로 나눈다.
	가운데를 기준으로 종이를 반 접어 겹친다 할 때
	왼쪽과 오른쪽이 한쪽은 0 반대쪽은 1이어야 함.
	이게 되면 성공.
	아니면 실패.
	'''
	if len(paper) == 1: return True

	mid = len(paper) // 2
	for i in range(mid):
		if paper[i] == paper[-1-i]:
			return False
	return canFold(paper[:mid])

# input & process & output
t = int(input())
for _ in range(t):
	paper = input().rstrip()
	print("YES" if canFold(paper) else "NO")