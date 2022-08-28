'''
다익스트라를 이용하면 2번 조건을 만족하는 경로들을 찾을 수 있음
1번 조건 해결책?
    슈퍼컴퓨터에서 나머지 컴퓨터들에 항상 접근할 수 있다고 할 때
    다익스트라 진행하면서 연결하는 선은 어차피 N-1개임
prev배열로 역추적하면 복구할 회선들도 알 수 있음
'''
import sys, heapq
input = sys.stdin.readline

# constant
INF = 12345

# input
num_pc, num_line = map(int, input().split())
lines = [[] for _ in range(num_pc + 1)]
for _ in range(num_line):
    A, B, C = map(int, input().split())
    lines[A].append((B, C))
    lines[B].append((A, C))

# process
# 다익스트라
visited = [False for _ in range(num_pc + 1)]
time = [INF for _ in range(num_pc + 1)]
prev = [i for i in range(num_pc + 1)]

h = [(0, 1)]
time[1] = 0

while h:
    t, cur = heapq.heappop(h)

    if visited[cur]: continue
    visited[cur] = True

    for next, c in lines[cur]:
        if not visited[next] and t + c < time[next]:
            time[next] = t + c
            prev[next] = cur
            heapq.heappush(h, (t + c, next))

# 역추적
restored_lines = set()

for pc in range(2, num_pc + 1):
    while pc != 1:
        restored_line = (pc, prev[pc]) if pc < prev[pc] else (prev[pc], pc)
        restored_lines.add(restored_line)
        pc = prev[pc]

# output
sol = [str(num_pc - 1)]
for a, b in restored_lines:
    sol.append(f'{a} {b}')
print('\n'.join(sol))