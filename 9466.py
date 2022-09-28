'''
사이클 찾는 문제

1. 임의의 학생 한 명을 골라 스택에 넣는다
2. 해당 학생이 가리킨 학생을 찾아 스택에 넣는다.
3. 만약 찾은 학생이 이미 스택에 있으면 사이클,
   찾은 학생이 pop될때까지 꺼내서 걔네는 조를 짠거고
   스택에 남아있는애들이 조가 없는애들

학생이 스택에 들어갔었는지 판단하는 visited배열 필요
특정 학생이 스택 안에 있는지를 판단하는 set 필요
'''

# input
T = int(input())
sol = []
for _ in range(T):
    n = int(input())
    pick = tuple(map(lambda x: int(x) - 1, input().split()))

    # process
    visited = [False for _ in range(n)]
    cnt = 0

    for student in range(n):
        if visited[student]: continue

        stack = [student]
        inside_stack = set(stack)

        while True:
            next = pick[stack[-1]]

            # 종료 조건
            if visited[next]: break
            elif next in inside_stack:
                while stack[-1] != next:
                    visited[stack.pop()] = True
                visited[stack.pop()] = True
                break

            # 스택에 넣기
            stack.append(next)
            inside_stack.add(next)

        cnt += len(stack)
        for i in stack:
            visited[i] = True

    sol.append(str(cnt))

# output
print('\n'.join(sol))