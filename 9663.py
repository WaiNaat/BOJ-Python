# function
def dfs(n):
    global cnt

    # base case
    if len(queen) == n:
        cnt += 1
        return
    
    # recursive step
    row = len(queen)
    for candidate in range(n):

        # 같은 열이 아니어야 함
        if candidate not in queen:

            # 대각선에 없어야 함
            isDiagonal = False
            for i in range(len(queen)):
                if candidate == queen[i] + (row - i) \
                    or candidate == queen[i] - (row - i):
                    isDiagonal = True
            
            # 최종 선정된 대상이 있으면 넣고 재귀
            if not isDiagonal:
                queen.append(candidate)
                dfs(n)
                queen.pop()


# input
n = int(input())

# process
'''
애초에 각 퀸은 행과 열이 모두 달라야 함!!

queen(i) := i번 열의 퀸이 위치한 행 번호
queen(0)부터 queen(n-1)까지 채운다 하면 열은 모두 다름.
그러면 백트래킹에서 검사해야 할 것은 행과 대각선.
'''
queen = []

cnt = 0
dfs(n)

# output
print(cnt)