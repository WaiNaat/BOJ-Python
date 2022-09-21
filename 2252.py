'''
topological sort

1. 자신의 child가 누구인지, parent가 몇 명인지 센다.
2. parent가 없는 애들부터 큐에 넣는다.
3. 큐에서 하나 꺼내서 child들의 parent수를 줄인다.
4. parent가 없는 child는 큐에 넣는다.
'''
import sys
input = sys.stdin.readline
from collections import deque

# input
N, M = map(int, input().split())
child = [set() for _ in range(N + 1)]
parent = [0 for _ in range(N + 1)]
for _ in range(M):
    smaller, taller = map(int, input().split())
    child[smaller].add(taller)
    parent[taller] += 1

# process
q = deque()
for student in range(1, N + 1):
    if parent[student] == 0:
        q.append(student)

sol = []
while q:
    cur = q.popleft()
    sol.append(cur)

    for next in child[cur]:
        parent[next] -= 1
        if parent[next] == 0:
            q.append(next)

# output
print(*sol)