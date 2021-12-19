import sys
sys.setrecursionlimit(10**6)

# functions
def DFS(cur, n):
	global cnt
	stone[cur] = -stone[cur] # 방문한 돌다리는 음수값으로 표시
	cnt += 1
	jump = -stone[cur]
	for next in (cur + jump, cur - jump):
		if not 0 <= next < n: # 돌다리 밖으로 나가는 경우
			continue
		if stone[next] > 0:
			DFS(next, n)

# input
n = int(input())
stone = list(map(int, input().split()))
s = int(input()) - 1
# process
cnt = 0
DFS(s, n)
# output
print(cnt)