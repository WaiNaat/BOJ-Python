# functions
def isValid(depth):
    for i in range(depth):
        # 같은 열에 없어야 함 & 대각선에 없어야 함
        if queen[depth] == queen[i] or abs(queen[depth] - queen[i]) == abs(depth - i):
            return False
    return True

def dfs(depth):
    global cnt, n

    # base case
    if depth == n:
        cnt += 1
        return
    
    # recursive step
    for candidate in range(n):
        # 같은 열이 아니어야 함
        if visited[candidate]:
            continue

        # 퀸 배치해봄
        queen[depth] = candidate
        
        # 유효성 검사
        if isValid(depth):
            visited[candidate] = True
            dfs(depth + 1)
            visited[candidate] = False


# input
n = int(input())

# process
'''
애초에 각 퀸은 행과 열이 모두 달라야 함!!

queen(i) := i번 열의 퀸이 위치한 행 번호
queen(0)부터 queen(n-1)까지 채운다 하면 열은 모두 다름.
그러면 백트래킹에서 검사해야 할 것은 행과 대각선.
'''
queen = [-1 for _ in range(n)]
visited = [False for _ in range(n)]
cnt = 0
dfs(0)

# output
print(cnt)