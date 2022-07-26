### 시간 초과 ###

import sys
input = sys.stdin.readline

# functions
def batting_order():
    global sol

    # base case
    if (len(batters) == 9):
        sol = max(sol, play_game())
        return
    
    # recursive step
    if (len(batters) == 3):
        batters.append(0)
        batting_order()
        batters.pop()
    else:
        for i in range(1, 9):
            if visited[i]: continue

            visited[i] = True
            batters.append(i)

            batting_order()

            batters.pop()
            visited[i] = False

def play_game():
    score = 0
    batter_idx = 0

    for inning in range(N):
        out = 0
        base = [False] * 4
        inning_info = info[inning]

        while out < 3:
            batter_result = inning_info[batters[batter_idx]]

            if batter_result == 0:
                out += 1
            else:
                base[0] = True

                for i in range(3, -1, -1):
                    if not base[i]: continue

                    if i + batter_result > 3:
                        score += 1
                    else:
                        base[i + batter_result] = True

                    base[i] = False

            batter_idx = (batter_idx + 1) % 9

    return score

# input
N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

# process
sol = 0
batters = []
visited = [False for _ in range(9)]

batting_order()

# output
print(sol)