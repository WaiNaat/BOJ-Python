# functions
def DFS(cur, n):
	visited = [0 for _ in range(n)]
	stack = [cur]
	cnt = 1
	visited[cur] = 1

	while stack:
		cur = stack.pop()
		jump = stone[cur]
		for next in (cur + jump, cur - jump):
			if not 0 <= next < n: # 돌다리 밖으로 나가는 경우
				continue
			if visited[next] == 0:
				visited[next] = 1
				cnt += 1
				stack.append(next)
	return cnt

# input
n = int(input())
stone = list(map(int, input().split()))
s = int(input()) - 1
# process & output
print(DFS(s, n))