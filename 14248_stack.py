# functions
def DFS(cur, n):
	stack = [cur]
	cnt = 1
	stone[cur] = -stone[cur] # 방문한 돌다리는 음수값으로 표시

	while stack:
		cur = stack.pop()
		jump = -stone[cur]
		for next in (cur + jump, cur - jump):
			if not 0 <= next < n: # 돌다리 밖으로 나가는 경우
				continue
			if stone[next] > 0:
				stone[next] = -stone[next]
				cnt += 1
				stack.append(next)
	return cnt

# input
n = int(input())
stone = list(map(int, input().split()))
s = int(input()) - 1
# process & output
print(DFS(s, n))