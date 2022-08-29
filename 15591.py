'''
그래프를 인접 배열로 만들고
bfs로 질문에 대한 답 찾기
'''
import sys
from collections import deque
input = sys.stdin.readline

# input
N, Q = map(int, input().split())
usado = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    p, q, r = map(int, input().split())
    usado[p].append((q, r))
    usado[q].append((p, r))
questions = [map(int, input().split()) for _ in range(Q)]

# process
sol = []
for k, v in questions:
    cnt = -1 # 본인은 제외

    q = deque([(v, 2147483647)])
    visited = [False for _ in range(N + 1)]

    while q:
        cur, cur_usado = q.popleft()
        
        if visited[cur]: continue
        visited[cur] = True
        cnt += 1

        for next, next_usado in usado[cur]:
            if not visited[next] and next_usado >= k:
                q.append((next, min(cur_usado, next_usado)))

    sol.append(str(cnt))

# output
print('\n'.join(sol))