'''
시작점을 c로 하는 다익스트라
'''
import sys, heapq
input = sys.stdin.readline

INF = 12345678

test_case = int(input())
sol = []

for _ in range(test_case):

    # input
    n, d, c = map(int, input().split())
    E = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        E[b].append((a, s))
        
    # process
    time = [INF for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    h = [(0, c)]

    time[c] = 0

    while h:
        t, cur = heapq.heappop(h)

        if visited[cur]: continue
        visited[cur] = True

        for next, s in E[cur]:
            if not visited[next] and t + s < time[next]:
                time[next] = t + s
                heapq.heappush(h, (t + s, next))

    cnt = 0
    total_time = 0
    for t in time:
        if t != INF:
            cnt += 1
            total_time = max(total_time, t)

    # output
    sol.append(f'{cnt} {total_time}')

print('\n'.join(sol))